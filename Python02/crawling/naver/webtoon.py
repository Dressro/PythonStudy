# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import json

url = "https://comic.naver.com/webtoon/weekdayList.nhn?week=thu"

resp = requests.get(url)
# print(resp.text)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)
webtoons = soup.find('ul', class_="img_list")
webtoon = webtoons.find_all('li')

lst = list()
for web in webtoon:
    #print("{} [{}]".format(web.find('dt').find('a').text, web.find('div', class_="rating_type").find("strong").text))
    tmp = {}
    tmp['title']=web.find('dt').find('a').text
    tmp['star']=web.find('div', class_="rating_type").find("strong").text
    lst.append(tmp)

#print(lst)

res = {}
res['webtoons'] = lst 

res_json = json.dumps(res,ensure_ascii=False)
#print(res_json)

with open('webtoon.json','w',encoding='utf-8') as f:
    f.write(res_json)