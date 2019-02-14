from flask import Flask, render_template, request, jsonify, redirect, url_for

import os

app = Flask(__name__)
server_name = os.getenv('SRV_NAME')

@app.route("/", methods=["GET"])
def get_my_ip():

    return jsonify({'ip': request.headers}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
