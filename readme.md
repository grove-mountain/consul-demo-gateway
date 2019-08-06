# Consul Demo Gateway

This is a basic web gateway written in Flask and styled with Bootstrap.   

The web gateway serves two applications

Docker image: grovemountain/consul-demo-gateway

## Consul Template Rendered Static page

The static app loads some JSON data that comes from Consul from the ./static directory.   The format of the data payloads are included in the monty_python.json file in this repo.   Flask reads the JSON payload.  I've also included a rendered HTML fragment.   Feel free to render either just the JSON file or JSON and the HTML fragment.   

## Consul Connect Layer 4

Docker Image: grovemountain/picture-service

This application is inspired by my daughter and her friends from school that play a game called "Pet Shop".

The Connect demo uses a generic image server as a backend/upstream.   The application is very simple and takes two main arguments: NAME, VERSION.   Currently, there are three "services": dogs, cats and rabbits.  You should launch three containers, one for each pet service and hook up the connect endpoints.   The VERSION parameter controls the number of pets served in each image to give a visual representation 

Check the app/static.py for the default upstreams.

For Layer 4, if you have things configured correctly each pet category will show the proper pet.

Page reloads will randomly load a new pet.   

## Consul Connect Layer 7

This extends the previous example but adds in Layer 7 Routing.   Change route distribution to 50/50 (or whatever percentage you wnt) so that subsequent reloads should load either N or N+1 pets in a window.  

