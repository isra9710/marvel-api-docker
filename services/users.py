import hashlib
from database import mycol
from flask import Flask, session

def start_session(user):
    session['logged_in'] = True
    session['user'] = user
    session['token'] = user['token']


def create_users(email, name, age, password):
    hashed = hashlib.md5( (password).encode('utf-8')).hexdigest()
    user_input = {'name': name,'email':email, 'age':age,'password': hashed, 'comics':[]}
    mycol.insert_one(user_input)
    user_found = mycol.find_one({'email':email})
    token = str(user_found['_id'])
    user_return = {'name': name,'email':email, 'age':age, "token":token}
    start_session(user_return)
    return {"code":200,"message":"Usuario registrado", "user":user_return}


def check_users(name, password):
    user_found = mycol.find_one({'name':name})
    if(user_found):
        hashed = hashlib.md5( (password).encode('utf-8')).hexdigest()
        password_stored = user_found['password']
        if (hashed == password_stored):
            token = str(user_found['_id'])
            name = user_found['name']
            email  = user_found['email']
            age = user_found['age']
            user_return = {'name': name,'email':email, 'age':age, "token":token}
            return {"code":200,"message":"Aquí están tus datos", "user":user_return}
        else:
            return {"code":404,"message":"Correo o contraseña incorrectos"}
    else:
        return {"code":404,"message":"Correo o contraseña incorrectos"}

def login_users(email, password):
    if "user" in session:
        user_return = session['user']
        return {"code":200,"message":"Ya hay una sesión iniciada", "user":user_return}
    user_found = mycol.find_one({'email':email})
    if(user_found):
        hashed = hashlib.md5( (password).encode('utf-8')).hexdigest()
        password_stored = user_found['password']
        if (hashed == password_stored):
            token = str(user_found['_id'])
            name = user_found['name']
            email  = user_found['email']
            age = user_found['age']
            user_return = {'name': name,'email':email, 'age':age, "token":token}
            start_session(user_return)
            return {"code":200,"message":"Has iniciado sesión", "user":user_return}
        else:
            return {"code":404,"message":"Correo o contraseña incorrectos"}
    else:
        return {"code":404,"message":"Correo o contraseña incorrectos"}



def logout_users():
    if "user" in session:
        session.pop("user", None)
        return {"code":200,"message":"Has cerrado sesión"}     
    else:
         return {"code":400,"message":"No hay sesión iniciada"}
   