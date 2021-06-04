# -*- coding:utf-8 -*-

from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/crawling')
def result_json():
    # https://movie.naver.com/movie/running/current.nhn
    # 제목, 별점을 {'title' : 제목 , 'star' : 별점} 형태로 크롤링 하여
    # {'movies':[{}] } 형태로 json 객체를 만들어서 리턴하자.
    url = "https://movie.naver.com/movie/running/current.nhn"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text , "html.parser")
    movies = soup.find_all('dl', class_="lst_dsc")
    movie_list = list()

    for movie in movies:
        mo_dict = dict()
        mo_dict['title'] = movie.find('a').text
        mo_dict['star'] = movie.find('span', class_='num').text
        movie_list.append(mo_dict)
    
    movie_dict = {'movies':movie_list}
    movie_json = json.dumps(movie_dict, ensure_ascii=False)
    
    return movie_json


if __name__ == "__main__":
    app.run(host='localhost', port='8686')

