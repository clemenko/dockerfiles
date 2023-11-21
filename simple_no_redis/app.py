from flask import Flask, render_template, request, jsonify, redirect, url_for

import os

version = "0.1"
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
    return jsonify({'redis': 'up'}), 200

@app.route('/info')
def info(server_name=None):
    return jsonify({'hostname': os.getenv('HOSTNAME'), 'version': version}), 200

@app.route('/version')
def version():
    return '2.0', 200

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.headers.get('X-Forwarded-For', '')}), 200

@app.route('/secret')
def secret():
    return red_word

@app.route('/')
def index(server_name=None):
    server_name = os.getenv('HOSTNAME')
    return render_template('index.html', server_name=server_name, ip=request.remote_addr, word=red_word) 

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)

