#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_byshf_zjb
活动名称: 百元生活费-赚金币-助力
Author: SheYu09
cron: 5 0 * * * jd_byshf_zjb.py
new Env('极速版 -*- 赚金币')
'''
import jdCookie, HEADERS, posturl, requests, json, time

def getShareCode(purl, bodys1, bodys2, bodys3, header):
    try:
        body = f'{bodys1}inviteTaskHomePage{bodys2}{bodys3}'
        r = requests.post(url=purl, headers=header, data=body).json()
        if r['data']['inviterNick'] == 'jd_***' and r['message'] == 'success':
            encryptionInviterPin = r['data']['encryptionInviterPin']
            return encryptionInviterPin
    except Exception as e:
        print("a获取互助码失败！", e)
        print()
        return 0

def helpCode(purl, bodys1, bodys2, bodys3, header, encryptionInviterPin, uNUm, user, name):
    print(f'====用户{uNUm} {user} 助力====')
    try:
        body = f'{bodys1}participateInviteTask{bodys2},"encryptionInviterPin":"{encryptionInviterPin}","type":1{bodys3}'
        r = requests.post(url=purl, headers=header, data=body).json()
        if r['message'] == 'success':
            print()
            print(r["message"])
            print(f'您也获得: {r["data"]["coinReward"]}金币')
        else:
            print()
            print(r["message"])
    except Exception as e:
        print()
        print("helpCode Error", e)
        print('报错了！')

def start():
    global cookiesList, pinNameList, ckNum
    print('    ******* 百元生活费-赚金币-助力 *******')
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
        purl, body1, body2 , body3 = posturl.jd_byshf()
        encryptionInviterPin = getShareCode(purl, body1, body2, body3, HEADERS.jd_byshf(cookiesList[ckNum]))
        if encryptionInviterPin == 0:
            print(f"===【京东账号】{pinNameList[int(ckNum)]}  获取互助码失败。请稍后再试！==")
            print()
            time.sleep(0.1)
            continue
        u = 0
        for i in cookiesList:
            if i == cookiesList[ckNum]:
                u += 1
                continue
            helpCode(purl, body1, body2, body3 , HEADERS.jd_byshf(i), encryptionInviterPin, u+1, pinNameList[u], pinNameList[ckNum])
            print()
            time.sleep(0.1)
            u += 1
  
if __name__ == '__main__':
    start()

