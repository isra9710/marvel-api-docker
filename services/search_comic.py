from email.mime import image
from keys import public_key, private_key
from config import url_search_comic_id, url_search_comic_title, ts
import hashlib
import requests
hashed = hashlib.md5( (str(ts) + private_key + public_key ).encode('utf-8')).hexdigest()
ts_string = "ts=" + str(ts)
ts_string_1 = "&ts=" + str(ts)
public_key_string = "&apikey=" + public_key
hashed_string = "&hash=" + str(hashed)
complement = ts_string_1 + public_key_string + hashed_string
complement_A_Z = ts_string + public_key_string + hashed_string


###Retorna la construcción del comic
def returnComic(response= None, comic_sended = None):
    data_comic = None
    if (response):
        json_load = response.json()
        data_comic = json_load['data']
        data_comic = data_comic['results'][0]
    else:
        data_comic = comic_sended
    print(data_comic)
    image = None
    if (len(data_comic['images'])>0):
        image = data_comic['images'][0]
    comic = {
            "id": data_comic['id'],
            "title": data_comic['title'],
            "image": image,
            "onsaleDate": data_comic['dates'][0]
            }
    return comic

#Busqueda por id de comic################
def searchComicId(comic_id):
    print("Search comic")
    comic_string = str(comic_id) + "?"
    url_id_comic = url_search_comic_id +  comic_string + complement
    response = requests.get(url_id_comic)
    if (response.status_code ==200):
        comic = returnComic(response)
        return{"code":200, "Comic":comic}
    else:
        return {"code":"404", "Comic":"No encontrado"}

#Busqueda por titulo de comic############
def searchComicTitle(title):
    title_string = "title=" + title
    url_title = url_search_comic_title + title_string + complement
    response = requests.get(url_title)
    if (response.status_code ==200):
        comic = returnComic(response)
        return{"code":200, "Comic":comic}
    else:
        return {"code":"404", "Comic":"No encontrado"}


def searchComicStartsWith(titleStartsWith):
    title_starts_with_string = "titleStartsWith=" +titleStartsWith
    url_comic_starts_with = url_search_comic_title + title_starts_with_string + complement
    response = requests.get(url_comic_starts_with)
    if (response.status_code == 200):
        json_load = response.json()
        comics_list_dict = json_load['data']['results']
        comics = []
        for comic in comics_list_dict:
            body_comic = returnComic(comic_sended=comic)
            comics.append(body_comic)
        return{"code":200, "Comics":comics}
    else:
        return {"code":404, "Comics":"No encontrado"}


def searchComicAZ():
    url_all_comics = url_search_comic_title + complement_A_Z
    response = requests.get(url_all_comics)
    if (response.status_code == 200):
        json_load = response.json()
        comics_list_dict = json_load['data']['results']
        comics = []
        for comic in comics_list_dict:
            body_comic = returnComic(comic_sended=comic)
            comics.append(body_comic)
        return{"code":200, "Comics":comics}
    else:
        return {"code":404, "Comics":"No encontrado"}
