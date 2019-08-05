import os
import glob
import random
from flask import Flask
from flask import render_template, send_file, current_app
import json
import petshop

# Be the main frame for all applications
# Loads static page into one tab
# Loads dynamic page into the second tab
# Dynamic page requests picture data from the picture-service app

BIND_HOST='0.0.0.0'
BIND_PORT=8000

app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return 'OK'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consul-template/')
def consul_template():
    context={}
    context_file='static/holy_grail.json'
    try:
        with app.open_resource(context_file, 'r') as IF:
            context=json.load(IF)
    except Exception as e:
        print("JSON Input file {} missing".format(context_file))
        print(e)
    return render_template('consul-template.html', **context)


@app.route('/layer4-connect/')
def layer4_connect():
    """ Layer 4 demo techniques.  Probably needs one more layer of abstraction.
    """
    context = petshop.get_pet_shop()
    return render_template('layer4-connect.html', **context)

@app.route('/layer7-routing/')
def layer7_routing():
    return render_template('layer7-routing.html')

class Upstream:
    def __init__(self, service, address):
        """ Service is the name of the upstream service name.
        Address should be the connection string containing protocol, ip, port of the local upstream connection
        e.g. http://127.0.0.1:10000. 
        """
        self.address = address
        self.service = service

if __name__ == '__main__':
    host = os.environ.get('BIND_HOST', BIND_HOST)
    port = os.environ.get('BIND_PORT', BIND_PORT)
    app.run(host=host, port=port)