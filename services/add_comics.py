import email
from urllib import response
from database import mycol
from flask import Flask, session
from services.search_comic import searchComicId
from bson.objectid import ObjectId

def add_comic(id_comic):
    response = searchComicId(id_comic)
    if(response['code'] == 200):
        user = session['user']
        comic = response['Comic']
        user_find = mycol.find_one({'email':user['email']})
        if (len(user_find['comics']) == 0):
            print("USER")
            print(user)
            print("COMIC")
            print(comic)
            mycol.update_one({"_id" :user_find['_id'] },{"$push" : {"comics.$comics":[comic]}})
        else:
            comics = user_find['comics']
            for number in comics:
                if(comic in number):
                    return {"code":400, "message": "Ese comic ya se encuentra en tu colección"}
            else:
                mycol.update_one({"_id" :user_find['_id'] },{"$push" : {"comics":[comic]}})
                return{"code":200, "message": "comic agregado"}
    return{"code":400, "message": "Error"}
    