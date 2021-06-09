# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

# client
client = MongoClient('localhost',27017)
# db
test = client.test
# collection
score = test.score

cursor = score.find()

for doc in cursor:
    pprint.pprint(doc)

print('------------------------')

shin = score.find_one({'name':'신동엽'})
pprint.pprint(shin)

# 국어점수가 60점 보다 큰 도큐먼트들을 모두 출력하자
print("-------------------------")
kors = score.find({'kor':{'$gt':60}})

for kor in kors:
    pprint.pprint(kor)
    
print("-------------------------")
print('score collection 안에 있는 document의 총 갯수 :' , score.count_documents({}) )