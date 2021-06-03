# -*- coding:utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup

tag = input("search tag : ")

url = 'http://www.instagram.com/explore/tags/' + tag

driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')

driver.implicitly_wait(3)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div', class_='KL4Bh')

for img in img_list:
    print(img.img['src'])

driver.close()
driver.quit()
