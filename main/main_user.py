from multiprocessing.reduction import register
import requests
import hashlib
from flask import Flask, session
from workflow.workflow_user import run_workflow_user

def user(request):
    if (request.method == 'POST'):
        email = request.args.get('email')
        name = request.args.get('name')
        age = request.args.get('age')
        password = request.args.get('password')
        logout_user = request.args.get('logout')
        if(logout_user):
            return run_workflow_user(request = request,logout_user=logout_user)
        if (not(email) or not (password) or not (name) or not (age)):
            return {"code:":"Error, en usuario, edad ,correo o contraseña", "status":400}
        else:
            register = True
            return run_workflow_user(request = request, register=register)
    if (request.method == 'GET'):
        email = request.args.get('email')
        password = request.args.get('password')
        login_user = request.args.get('login')
        check_user = request.args.get('check_user')
        name = request.args.get('name')
        if(check_user):
            if(not (name)):
                return {"code:":"Error, necesitas nombre y contraseña recibir tus datos", "status":400}
            else:
                return run_workflow_user(request = request, check_user = check_user)
        if (not(email) or not (password)):
            return {"code:":"Error, necesitas correo y contraseña para autentificar", "status":400}
        if (login_user):
            return run_workflow_user(request = request, login_user=login_user)
    return {"code":400, "status":"El metodo solo pude ser GET o POST"}