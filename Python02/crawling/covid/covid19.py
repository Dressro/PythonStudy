# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="

resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'html.parser')

peo = soup.find("div",class_="caseTable").find_all("li")[1].find_all("p",class_="inner_value")

#print(peo[1].text)
#print(peo[2].text)



#print(kor_peo)
#print(for_peo)

result = '''국내발생 : {}
해외유입 : {}
소 계 : {}
'''.format(peo[1].text,peo[2].text,peo[0].text.split(' ')[1])

print(result)