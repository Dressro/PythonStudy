# -*- coding:utf-8 -*-

# pip install beautifulsoup4
from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
soup = BeautifulSoup(resp,'html.parser')

#print(soup)

movies = soup.find_all('dl', class_='lst_dsc')

# movies 안에 있는 제목과 별점을 파싱해서
# 제목 [별점]으로 반복해서 출력하자
for movie in movies:
    print(movie.find('a').text)
    print(movie.find('span', class_="num").text)