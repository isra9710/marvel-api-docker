#from api_search_comics.main import search_comic
#from api_search_comics.workflow.workflow import run_workflow
from cProfile import run
from urllib import response
import bcrypt, json, requests, hashlib, pymongo, re
from flask import Flask, request
from flask import Flask, render_template, request, url_for, redirect, session
from pymongo import server
from main.main_comic import search_comic
from main.main_user import user
from main.main_add_comics import add_comic
from main.main_get_comics import get_comic


app = Flask(__name__)
app.secret_key = "coppelApp22"


if __name__ == '__main__':
    app.run(host = 'localhost', port = 8088, debug = True)
    
@app.route("/", methods= ['GET'])
def hello_world(request):
    if (request.method == 'GET'):
        print(request.args.get('saludo'))
        return "<p>Hello, World!</p>"
###URL para consumir los servicios del buscador de comics o personajes
@app.route("/searchComics" , methods=['GET'])
def searchComics():
    if (request.method == 'GET'):
        response = search_comic(request)
        return response    
    return {"code":400, "status":"Esta petición es GET"}

###URL para el consumo de inicio de sesión, ver credenciales, cerrar sesión
@app.route("/users" , methods=['POST','GET'])
def users():
    if (request.method == 'POST'):
        response = user(request)
        return response
    
    if (request.method == 'GET'):
        response = user(request)
        return response
    return {"code":400, "status":"Error en la petición"}
    
###URL para agregar comics por id
@app.route("/addToLayaway" , methods = ['POST'])
def add_comics():
    if "user" in session:
        if (request.method == 'POST'):
            response = add_comic(request)
            return response
    else:
        return {"code":400, "message":"Inicia sesión para agregar comics"}        
    return {"code":400, "status":"Esta petición es POST"}



###URL visualizar comics por usuario

@app.route("/getToLayaway" , methods = ['GET'])
def get_comics():
    if "user" in session:
        if (request.method == 'GET'):
            response = get_comic(request)
            return response
    else:
        return {"code":400, "message":"Inicia sesión para ver comics"}        
    return {"code":400, "status":"Esta petición es GET"}