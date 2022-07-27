from database import mycol
from flask import Flask, session
import flask
import pymongo
import hashlib
from services.users import create_users, login_users, logout_users, check_users


def run_workflow_user(request, register = None, check_user = None, login_user = None, logout_user = None):
    if(register is True):
        email = request.args.get('email')
        name = request.args.get('name')
        age = request.args.get('age')
        password = request.args.get('password')
        user_found = mycol.find_one({'email':email})
        user_name = mycol.find_one({'name':name})
        if(user_found or user_name):
            return {"code":400,"message":"Correo o usuario ya registrados"}
        else:
            return create_users(email, name, age, password)
    if(check_user is True):
        print("ENTRA AL CHECK USER")
        name = request.args.get('name')
        password = request.args.get('password')
        return check_users(name, password)
    
    if(login_user is True):
      email = request.args.get('email')
      password = request.args.get('password')
      return login_users(email, password)
        
    if (logout_user is True):
        return logout_users()
