#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_jx88hb
活动名称: 领88元红包-助力
Author: SheYu09
cron: 0 0 * * * jd_jx88hb.py
new Env('京喜 -*- 领88元红包')
'''
import requests, json, time, sys
sys.path.append('../repo/SheYu09_jd_scripts_master/')
import jdCookie, HEADERS, h5st, posturl, jd_jx88_chb

def getShareCode(purl, bodys, header):
    global aNum
    try:
        url = f'{purl}JoinActive{bodys}&h5st='
        url += h5st.start(url, '10010')
        r = requests.get(url=url, headers=header).text
        data = json.loads(r)
        if data["iRet"] == 0:
            strUserPin = data["Data"]["strUserPin"]
            print(f'活动开启成功,助力邀请码为: {strUserPin}')
        else:
            print(f'活动开启失败: {data["sErrMsg"]}')
            url = f'{purl}GetUserInfo{bodys}&h5st='
            url += h5st.start(url, '10010')
            r = requests.get(url=url, headers=header).text
            data = json.loads(r)
            if data["iRet"] == 0:
                strUserPin = data["Data"]["strUserPin"]
                print(f'获取助力码成功: {strUserPin}')
        print()
        return strUserPin
    except Exception as e:
        if aNum < 5:
            aNum += 1
            return getShareCode(purl, bodys, header)
        else:
            aNum = 0
            print("获取互助码失败！", e)
            print()
            return 0

def helpCode(purl, bodys, header, strPin, uNUm, user):
    print(f'====用户{uNUm} {user} 助力====')
    print()
    try:
        url = f'{purl}EnrollFriend{bodys},strPin&strPin={strPin}&h5st='
        url += h5st.start(url, '10010')
        r = requests.get(url=url, headers=header).text
        data = json.loads(r)
        iRet = data["iRet"]
        if iRet == 0:
            print('            助力成功🎉')
            print(f'               {data["sErrMsg"]}')
        else:
            print('             助力失败')
            print(f'{data["sErrMsg"]}')
        print()
        return iRet
    except Exception as e:
        print()
        print("helpCode Error", e)
        print('报错了！')

def start():
    print('    ******* 领88元红包-助力 *******')
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
        purl, body = posturl.jd_jx88hb()
        strUserPin = getShareCode(purl, body, HEADERS.jd_jx88hb(cookiesList[ckNum]))
        if strUserPin == 0:
            print(f"===【京东账号】{pinNameList[int(ckNum)]}  获取互助码失败。请稍后再试！==")
            print()
            continue
        u = 0
        for i in cookiesList:
            if i == cookiesList[ckNum]:
                u += 1
                continue
            iRet = helpCode(purl, body, HEADERS.jd_jx88hb(i), strUserPin, u+1, pinNameList[u])
            if iRet == 2013:
                # jd_jx88_chb.start()
                break
            time.sleep(0.01)
            u += 1

aNum = 0
if __name__ == '__main__':
    start()
