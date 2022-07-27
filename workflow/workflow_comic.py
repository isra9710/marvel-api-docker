from config import url_search_character_id
from services.search_character import searchCharacterId, searchCharacterName, searchCharacterStartsWith, searchCharacterAZ
from services.search_comic import searchComicId, searchComicStartsWith, searchComicTitle, searchComicAZ 
from flask import Flask, request
import requests
def run_workflow_comic(request):
    id_comic = request.args.get('id_comic')
    id_character = request.args.get('id_character')
    title = request.args.get('title')
    name = request.args.get('name')
    titleStartsWith = request.args.get('titleStartsWith')
    nameStartsWith = request.args.get('nameStartsWith')
    comic = request.args.get('comic')
    character = request.args.get('character')
    if (comic):
        if (id_comic):
            return searchComicId(id_comic)
        elif(title):
            return searchComicTitle(title)
        elif(titleStartsWith):
            return searchComicStartsWith(titleStartsWith)
        else:
            return searchComicAZ()
    if (character):
        if (id_character):
            return searchCharacterId(id_character)
            
        elif(name):
            return searchCharacterName(name)
            
        elif(nameStartsWith):
            return searchCharacterStartsWith(nameStartsWith)
        else:
            return searchCharacterAZ()
    return{"status":"ok", "Entro":False}
