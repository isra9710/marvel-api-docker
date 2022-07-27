from urllib import response
import requests
from flask import request
from keys import public_key, private_key
from config import url_search_character_id, url_search_character_name, ts
import hashlib
import json


hashed = hashlib.md5( (str(ts) + private_key + public_key ).encode('utf-8')).hexdigest()
ts_string = "ts=" + str(ts)
ts_string_1 = "&ts=" + str(ts)
public_key_string = "&apikey=" + public_key
hashed_string = "&hash=" + str(hashed)
complement = ts_string_1 + public_key_string + hashed_string
complement_A_Z = ts_string + public_key_string + hashed_string

###Retorna la construcción del personaje
def returnCharacter(response= None, character_sended = None):
    data_character = None
    if (response):
        json_load = response.json()
        data_character = json_load['data']
        data_character = data_character['results'][0]
    else:
        data_character = character_sended
    print(data_character)
    character = {
            "id": data_character['id'],
            "name": data_character['name'],
            "image": data_character['thumbnail'],
            "appareances": data_character['comics']['available'] 
            }
    return character

#Busqueda por id de personaje################
def searchCharacterId(character_id):
    character_string = str(character_id) + "?"
    url_id_character = url_search_character_id +  character_string+ complement
    response = requests.get(url_id_character)
    if (response.status_code ==200):
        character = returnCharacter(response)
        return{"code":"200", "Personaje":character}
    else:
        return {"code":"404", "Personaje":"No encontrado"}
    

#Busqueda por titulo de personaje############
def searchCharacterName(name):
    name_string = "name=" + name
    url_name = url_search_character_name + name_string + complement
    response = requests.get(url_name)
    if (response.status_code ==200):
        character = returnCharacter(response)
        return{"status":"200", "Personaje":character}
    else:
        return {"status":"404", "Personaje":"No encontrado"}

### Busqueda por caracteres iniciales del personaje
def searchCharacterStartsWith(nameStartsWith):
    name_character_starts_with_string = "nameStartsWith=" + nameStartsWith
    url_character_starts_with = url_search_character_name + name_character_starts_with_string + complement
    response = requests.get(url_character_starts_with)
    if (response.status_code == 200):
        json_load = response.json()
        characters_list_dict = json_load['data']['results']
        characters = []
        for character in characters_list_dict:
            body_character = returnCharacter(character_sended=character)
            characters.append(body_character)
        return{"code":"200", "Personajes":characters}
    else:
        return {"code":"404", "Personajes":"No encontrado"}

###Busqueda de todos los personajes
def searchCharacterAZ():
    url_all_characters = url_search_character_name + complement_A_Z
    response = requests.get(url_all_characters)
    if (response.status_code == 200):
        json_load = response.json()
        characters_list_dict = json_load['data']['results']
        characters = []
        for character in characters_list_dict:
            body_character = returnCharacter(character_sended=character)
            characters.append(body_character)
        return{"code":"200", "Personajes":characters}
    else:
        return {"code":"404", "Personaje":"No encontrado"}




    