
from flask import Flask
from flask import render_template, send_file, current_app, url_for
import os
import json
import requests

""" Petshop returns the addresses of the pets being managed """
# Defaults for app using Consul Connect Proxies
DOGS_ADDR = 'http://127.0.0.1:42100'
CATS_ADDR = 'http://127.0.0.1:42200'
PARROTS_ADDR = 'http://127.0.0.1:42300'
RABBITS_ADDR = 'http://127.0.0.1:42400'
DEFAULT_PIC_SRC = 'images/petshop_default.png'

def get_pet_shop():

    dogs_address = os.environ.get('DOGS_ADDR', DOGS_ADDR)
    dogs_pic_src = get_picture_src(name='dogs', address=dogs_address)

    cats_address = os.environ.get('CATS_ADDR', CATS_ADDR)
    cats_pic_src = get_picture_src(name='cats', address=cats_address)

    rabbit_address = os.environ.get('RABBITS_ADDR', RABBITS_ADDR)
    rabbits_pic_src = get_picture_src(name='rabbits', address=rabbit_address)

    parrot_address = os.environ.get('PARROTS_ADDR', PARROTS_ADDR)
    parrots_pic_src = get_picture_src(name='parrots', address=parrot_address)

    return { "dogs_pic_src" :dogs_pic_src, 
             "cats_pic_src" : cats_pic_src, 
             "rabbits_pic_src" : rabbits_pic_src, 
             "parrots_pic_src" : parrots_pic_src }

def get_picture_src(name, address):
    """Queries the endpoint for a picture and returns the address if this is valid
    This prevents needing to handle the file locally
    """
    pic_src = url_for('static', filename=os.environ.get('DEFAULT_PIC_SRC', DEFAULT_PIC_SRC))
    print(pic_src)
    try:
        r = requests.get(address)
        if r.status_code == 200:
            pic_src = address
    except requests.ConnectionError as e:
        print(e)
    return pic_src