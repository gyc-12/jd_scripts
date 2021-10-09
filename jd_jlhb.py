#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_jlhb
活动名称: 锦鲤红包-助力
Author: SheYu09
cron: 0 0 * * * jd_jlhb.py
new Env('京东 -*- 锦鲤红包')
'''
import requests, time, sys
sys.path.append('../repo/SheYu09_jd_scripts_master/')
import jdCookie, HEADERS, posturl

def OpenActivity(purl, bodys, header):
    try:
        url = f'{purl}h5launch{bodys}'
        body = 'body={}'
        r = requests.post(url=url, headers=header, data=body).json()
        print(r["data"]["result"]["statusDesc"])
        print()
        return r["data"]["result"]["status"]
    except:
        print("黑号...")
        print()
        return 1
            

def getShareCode(purl, bodys, header):
    global aNum
    try:
        url = f'{purl}h5activityIndex{bodys}'
        body = 'body={}'
        r = requests.post(url=url, headers=header, data=body).json()
        redPacketId = r["data"]["result"]["redpacketInfo"]["id"]
        print(redPacketId)
        return redPacketId
    except Exception as e:
        if aNum < 5:
            aNum += 1
            return getShareCode(purl, bodys, header)
        else:
            aNum = 0
            print("获取互助码失败！", e)
            print()
            return 0

def helpCode(purl, bodys, header, redPacketId, uNUm, user):
    print(f'====用户{uNUm} {user} 助力====')
    print()
    try:
        url = f'{purl}jinli_h5assist{bodys}'
        body = 'body={' + f'"redPacketId":"{redPacketId}"' + '}'
        r = requests.post(url=url, headers=header, data=body).json()
        print(r["data"]["result"]["statusDesc"])
        print()
        return r["data"]["result"]["status"]
    except:
        print("黑号...")
        print()
        return 0

def start():
    print('          ******* 锦鲤红包-助力 *******')
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
        purl, body = posturl.jd_jlhb()
        status = OpenActivity(purl, body, HEADERS.jd_jlhb(cookiesList[ckNum]))
        if status == 1:
            continue
        redPacketId = getShareCode(purl, body, HEADERS.jd_jlhb(cookiesList[ckNum]))
        if redPacketId == 0:
            print(f"===【京东账号】{pinNameList[int(ckNum)]}  获取互助码失败。请稍后再试！==")
            print()
            time.sleep(0.1)
            continue
        u = 0
        for i in cookiesList:
            if i == cookiesList[ckNum]:
                u += 1
                continue
            status = helpCode(purl, body, HEADERS.jd_jlhb(i), redPacketId, u+1, pinNameList[u])
            time.sleep(0.1)
            if status == 2:
                break
            u += 1
  
aNum = 0
if __name__ == '__main__':
    start()
