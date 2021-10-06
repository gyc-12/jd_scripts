#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_jxcfd_hb
活动名称: 财富岛-合成珍珠红包-兑换
Author: SheYu09
'''
import jdCookie, HEADERS, h5st, posturl, requests, json

# 兑换红包金额
strPrizeName = 10

def ExchangePearlState(purl, bodys, header):
    url = f'{purl}user/ExchangePearlState{bodys}&_stk=strZone&h5st='
    url += h5st.start(url, '10032')
    r = requests.get(url=url, headers=header).text
    data = json.loads(r)['exchangeInfo']['prizeInfo']
    for i in data:
        if i['strPrizeName'] == f'{strPrizeName}元':
            ddwVirHb = i['ddwVirHb']
            dwLvl = i['dwLvl']
            strPool = i['strPool']
            return ddwVirHb, dwLvl, strPool
            break

def ExchangePearlHb(purl, bodys, header, ddwVirHb, dwLvl, strPoolName):
    url = f'{purl}user/ExchangePearlHb{bodys}&dwLvl={dwLvl}&ddwVirHb={ddwVirHb}&strPoolName={strPoolName}&_stk=ddwVirHb,dwLvl,strPoolName,strZone&h5st='
    url += h5st.start(url, '10032')
    r = requests.get(url=url, headers=header).text
    data = json.loads(r)
    print(data)

def start():
    global cookiesList, pinNameList, ckNum
    print()
    print('    ******* 财富岛-合成珍珠红包-兑换 *******')
    cookiesList, pinNameList = jdCookie.start()
    for ckname in jdCookie.Name():
        try:
            ckNum = pinNameList.index(ckname)
        except:
            print(f"请检查被助力账号【{ckname}】名称是否正确？提示：助力名字可填pt_pin的值、也可以填账号名。")
            continue
        print()
        print(f"*******开始【京东账号】{pinNameList[int(ckNum)]} *******")
        print()
        if strPrizeName not in [0.2, 1, 2, 5, 10, 100]:
            print('请输入正确兑换的红包金额...')
            exit()
        purl, body = posturl.jd_jxcfd()
        ddwVirHb, dwLvl, strPool = ExchangePearlState(purl, body, HEADERS.jd_jxcfd(cookiesList[ckNum]))
        ExchangePearlHb(purl, body, HEADERS.jd_jxcfd(cookiesList[ckNum]), ddwVirHb, dwLvl, strPool)
