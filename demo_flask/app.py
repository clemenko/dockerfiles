from flask import Flask, render_template, request, jsonify, redirect, url_for
from redis import Redis
from pymongo import MongoClient

import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
server_name = os.getenv('HOSTNAME')
server_health_key = '{0}_health'.format(server_name)

if os.path.isfile('/run/secrets/demo_title'):
   open('/run/secrets/demo_title', 'r')
   title = open('/run/secrets/demo_title', 'r')
   red_secret = title.read()
   title.close
else:
   red_secret = 'you should use secrets.'

client = MongoClient('mongo')
db = client.ipdb

@app.route('/health/on')
def health_on():
    redis.set(server_health_key, 'on')
    return 'Health key {0} set to on!'.format(server_health_key)

@app.route('/health/off')
def health_off():
    redis.set(server_health_key, 'off')
    return 'Health key {0} set to off!'.format(server_health_key)

@app.route('/healthz')
def health_check():
    health = redis.get(server_health_key)
    if health == 'on':
        return jsonify({'redis': 'up', 'mongo': 'up'}), 200
    else:
        return jsonify({'redis': 'down', 'mongo': 'down'}), 500

@app.route('/info')
def info(server_name=None):
    server_name = os.getenv('HOSTNAME')
    return server_name + ' : 0.1', 200

@app.route('/headers')
def headers():
    print request.__dict__
    return 'printed to log', 200

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    print jsonify({'ip': request.headers.get('X-Forwarded-For', '')}), 200
    print request.headers.get("X-Forwarded-Host")
    print request.remote_addr
    return jsonify({'ip': request.headers.getlist("X-Forwarded-For")})
    #X-Real-IP

@app.route('/list')
def listip():
    server_name = os.getenv('HOSTNAME')
    _items = db.ipdb.find()
    items = [item for item in _items]
    return render_template('list.html', items=items, hits=redis.get('hits'), server_name=server_name)

@app.route('/secret')
def secret():
    return red_secret

@app.route('/')
def index(server_name=None):
    redis.incr('hits')
    server_name = os.getenv('HOSTNAME')
    item_doc = {
        'ip': request.remote_addr
    }
    db.ipdb.insert_one(item_doc)
    return render_template('index.html', hits=redis.get('hits'), server_name=server_name, ip=request.remote_addr, secret=red_secret)

if __name__ == '__main__':
    health_on()
    app.run(host='0.0.0.0')
