from flask import Flask, render_template, request, jsonify, redirect, url_for

import os

app = Flask(__name__)
server_name = os.getenv('SRV_NAME')

if os.path.isfile('/run/secrets/demo_title'):
   open('/run/secrets/demo_title', 'r')
   title = open('/run/secrets/demo_title', 'r')
   red_secret = title.read()
   title.close
else:
   red_secret = 'you should use secrets.'

@app.route('/healthz')
def health_check():
    if health == 'on':
        return jsonify({'redis': 'up', 'mongo': 'up'}), 200
    else:
        return jsonify({'redis': 'down', 'mongo': 'down'}), 500

@app.route('/info')
def info(server_name=None):
    redis.incr('hits')
    return jsonify(os.getenv('HOSTNAME'),redis.get('hits').decode('utf-8'),version), 200

@app.route('/version')
def version():
    return '2.0', 200

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.headers.get('X-Forwarded-For', '')}), 200

@app.route('/secret')
def secret():
    return red_secret

@app.route('/')
def index(server_name=None):
    server_name = os.getenv('HOSTNAME')
    return render_template('index.html', server_name=server_name, ip=request.remote_addr, secret=red_secret)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
