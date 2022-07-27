from flask import session
from database import mycol
from flask import Flask, session
from datetime import datetime

def get_comics(fecha = None, alfabetico = None):
    user = session['user']
    user_find = mycol.find_one({'email':user['email']})
    if (len(user_find['comics'])> 0):
        comics = user_find['comics']
        new_list_comics = []
        for comic in comics:
            print(comic)
            datem = comic[0]['onsaleDate']['date']
            datem = datem[0:10]
            comic[0]['onsaleDate']['date'] = datem
            new_list_comics.append(comic[0])
        comics = new_list_comics
        print(type(comics))
        if (fecha):
            print("ANTES DE ORDENAR POR FEHCA")
            print(comics)
            sorted_comics_date = sorted(comics, key=lambda c: datetime.strptime(c['onsaleDate']['date'], '%Y-%m-%d'))
            print("DESPUES")
            print(sorted_comics_date)
            return {"code":200, "message":"Éstos son tus comics ordenados por fecha","comics":sorted_comics_date} 
        if(alfabetico):
            sorted_comics_alphabetic = sorted(comics, key=lambda x: x['title'])
            print("ANTES DE ORDENAR POR TITULO")
            print(comics)
            print("DESPUES")
            print(sorted_comics_alphabetic)
            return {"code":200, "message":"Éstos son tus comics ordenados por alfabeto","comics":sorted_comics_alphabetic}
        return {"code":200, "message":"Éstos son todos tus comics","comics":comics}    
    else:
        return {"code":200, "message":"No tienes comics almacenados"}