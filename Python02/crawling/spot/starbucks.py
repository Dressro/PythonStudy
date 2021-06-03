# -*- coding:utf-8 -*-

import requests
import json

# https://www.starbucks.co.kr


def getSido():
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    resp = requests.post(url)
    # print(resp.json()['list'][0])
    sido_json = resp.json()['list']
    sido_code = list(map(lambda x: x['sido_cd'], sido_json))
    sido_name = list(map(lambda x: x['sido_nm'], sido_json))

    sido_dict = dict(zip(sido_code,sido_name))
    return sido_dict
    

def getGuGun(sido_code):
    url = "https://www.starbucks.co.kr/store/getGugunList.do"
    resp = requests.post(url,data={'sido_cd':sido_code})
    gugun_json = resp.json()['list']
    gugun_code = list(map(lambda x : x['gugun_cd'],gugun_json))
    gugun_name = list(map(lambda x : x['gugun_nm'],gugun_json))
    
    gugun_dict = dict(zip(gugun_code,gugun_name))
    return gugun_dict


def getStore(sido_code='',gugun_code=''):
    url="https://www.starbucks.co.kr/store/getStore.do"
    resp = requests.post(url,data={
            'ins_lat':'37.56682',
            'ins_lng':'126.97865',
            'p_sido_cd':sido_code,
            'p_gugun_cd':gugun_code,
            'in_biz_cd':'',
            'set_date':''
        })
    store_json = resp.json()['list']
    lst = list()
    str_dict = dict()
    count = 0
    for store in store_json:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        lst.append(store_dict)
        count += 1

    str_dict['store_list'] = lst
    str_dict['count'] = count
    return str_dict


if __name__ == "__main__":
    print(getSido())
    sido = input("도시 코드를 입력해주세요 :")
    if sido == 17 :
        pass
    else:
        print(getGuGun(sido))
        gugun = input('구군 코드를 입력해주세요 :' )
        print(getStore(gugun_code=gugun))
