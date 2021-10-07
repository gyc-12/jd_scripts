#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_tyt
活动名称: 推一推-助力
Author: SheYu09
cron: 0 0 * * * jd_tyt.py
new Env('极速版 -*- 推一推')
'''
import jdCookie, HEADERS, posturl, h5st, requests, json, time

def getShareCode(purl, bodys1, bodys2, header):
    try:
        body = f'functionId=initiateCoinDozer{bodys1}{bodys2}megatron'
        r = requests.post(url=purl, headers=header, data=body).json()
        if r['code'] == 0 and r['msg'] == 'OK':
            packetId = r['data']['packetId']
            print(f'********** 活动发起: {r["msg"]} **********')
            print()
            print(f'获得：{r["data"]["amount"]}')
            print()
            print('********** 逛会场: 两秒 **********')
            print()
            body1 = f'functionId=coinDozerBackFlow{bodys1}{bodys2}megatron'
            r1 = requests.post(url=purl, headers=header, data=body1).json()
            time.sleep(2)
            if r1['code'] == 0 and r1['msg'] == 'OK':
                print('获得：再推一次')
            else:
                print("获取: 再推一次 失败！", e)
            print()
        elif r['code'] == 701:
            body2 = f'functionId=getCoinDozerInfo{bodys1}{bodys2}megatron'
            r2 = requests.post(url=purl, headers=header, data=body2).json()
            if r2['code'] == 0 and r2['msg'] == 'OK':
                packetId = r2['data']['sponsorActivityInfo']['packetId']
        if r['code'] != 703:
            return packetId
        else:
            return 703
    except Exception as e:
        if aNum < 5:
            aNum += 1
            return getShareCode(purl, bodys1, bodys2, header)
        else:
            aNum = 0
            print("获取互助码失败！", e)
            print()
            return 0

def helpCode(purl, bodys1, bodys2, header, packetId, uNUm, user):
    print(f'====用户{uNUm} {user} 助力====')
    print()
    try:
        body = f'functionId=helpCoinDozer{bodys1},"packetId":"{packetId}"{bodys2}station-soa-h5&_stk=appid,body,functionId&h5st='
        body += h5st.start(body, '10005')
        r = requests.post(url=purl, headers=header, data=body).json()
        code = r['code']
        if code == 0 and r['msg'] == 'OK':
            print(r["msg"])
            print(f'帮砍：{r["data"]["amount"]}')
        else:
            print(r["msg"])
        print()
        return code
    except Exception as e:
        print("helpCode Error", e)
        print('报错了！')
        print()

def start():
    print('          ******* 推一推-助力 *******')
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
        purl, body1, body2 = posturl.jd_tyt()
        packetId = getShareCode(purl, body1, body2, HEADERS.jd_tyt(cookiesList[ckNum]))
        if packetId == 0:
            print(f"===【京东账号】{pinNameList[int(ckNum)]}  获取互助码失败。请稍后再试！==")
            print()
            time.sleep(10)
            continue
        elif packetId == 703:
            print("已完成砍价")
            print()
            continue
        u = 0
        for i in cookiesList:
            code = helpCode(purl, body1, body2, HEADERS.jd_tyt(i), packetId, u+1, pinNameList[u])
            if code == 703:
                break
            time.sleep(10)
            u += 1
  
aNum = 0
if __name__ == '__main__':
    start()
