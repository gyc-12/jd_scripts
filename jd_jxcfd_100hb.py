#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_jxcfd_100hb
活动名称: 财富岛-100元红包-兑换
Author: SheYu09
cron: 0 0,10 * * * jd_jxcfd_100hb.py
new Env('京喜 -*- 财富岛100元红包')
'''
import requests, json, os, sys
sys.path.append('../repo/SheYu09_jd_scripts_master/')
import jdCookie, HEADERS, h5st, posturl

def ExchangeState(header):
    url = 'https://m.jingxi.com/jxbfd/user/ExchangeState?strZone=jxbfd&dwType=2&_stk=dwType,strZone&sceneval=2&h5st='
    url += h5st.start(url, '10032')
    r = requests.get(url=url, headers=header).text
    data = json.loads(r)
    hongbaopool = data["hongbaopool"]
    hongbao = data["hongbao"]
    for i in hongbao:
        if i["strPrizeName"] == '100元':
            ddwPaperMoney = i['ddwPaperMoney']
            dwLvl = i['dwLvl']
            break
    return hongbaopool, ddwPaperMoney, dwLvl

def ExchangePrize(header, strPoolName, ddwPaperMoney, dwLvl):
    url = f'https://m.jingxi.com/jxbfd/user/ExchangePrize?strZone=jxbfd&dwType=3&dwLvl={dwLvl}&ddwPaperMoney={ddwPaperMoney}&strPoolName={strPoolName}&_stk=ddwPaperMoney,dwLvl,dwType,strPoolName,strZone&sceneval=2&h5st='
    url += h5st.start(url, '10032')
    r = requests.get(url=url, headers=header).text
    data = json.loads(r)
    print(data)
    if data['iRet'] == 0:
        print(f'{data["strAwardDetail"]["strName"]}')
    else:
        print(f'{data["sErrMsg"]}')
    print()

def start():
    print('    ******* 财富岛-100元红包-兑换 *******')
    print()
    cookiesList, pinNameList = jdCookie.start()
    for ckname in jdCookie.Name():
        try:
            ckNum = pinNameList.index(ckname)
        except:
            print(f"请检查被助力账号【{ckname}】名称是否正确？提示：助力名字可填pt_pin的值、也可以填账号名。")
            print()
            continue
        print(f"*******开始【京东账号】{pinNameList[int(ckNum)]} *******")
        print()
        hongbaopool, ddwPaperMoney, dwLvl = ExchangeState(HEADERS.jd_jxcfd(cookiesList[ckNum]))
        ExchangePrize(HEADERS.jd_jxcfd(cookiesList[ckNum]), hongbaopool, ddwPaperMoney, dwLvl)

if __name__ == '__main__':
    start()
