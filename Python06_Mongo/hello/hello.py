# -*- coding:utf-8 -*-

from pymongo import MongoClient


client = MongoClient('localhost', 27017)

db = client.test

collection = db.score

result = collection.find()
#print(result)

for res in result:
    print(res)