#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_jxfhb
活动名称: 订单返红包-助力
Author: SheYu09
cron: 0 10 1/1 * * jd_jxfhb.py
new Env('京喜 -*- 订单返红包')
'''
import jdCookie, HEADERS, h5st, posturl, requests, json, time

def getShareCode(purl, bodys, header):
    try:
        url = f'{purl}QueryGroupDetail?orderid={orderid}{bodys}'
        r = requests.get(url=url, headers=header).text
        data = json.loads(r)
        return data["data"]["groupinfo"]["groupid"]
        """
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
        """
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
        url = f'{purl}Help?groupid={groupid}{bodys}&_stk=groupid&h5st='
        url += h5st.start(url, '10022')
        r = requests.get(url=url, headers=header).text
        data = json.loads(r)
        if data["msg"] == "":
            print('            助力成功🎉')
            print(f'               {data["systime"]}')
        else:
            print('             助力失败')
            print(f'{data["msg"]}')
        print()
    except Exception as e:
        print()
        print("helpCode Error", e)
        print('报错了！')

def start():
    print('    ******* 订单返红包-助力 *******')
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
        purl, body = posturl.jd_jxfhb()
        groupid = getShareCode(purl, body, HEADERS.jd_jxfhb(cookiesList[ckNum]))
        if groupid == 0:
            print(f"===【京东账号】{pinNameList[int(ckNum)]}  获取互助码失败。请稍后再试！==")
            print()
            continue
        u = 0
        for i in cookiesList:
            if i == cookiesList[ckNum]:
                u += 1
                continue
            helpCode(purl, body, HEADERS.jd_jxfhb(i), groupid, u+1, pinNameList[u])
            time.sleep(0.01)
            u += 1

aNum = 0
if __name__ == '__main__':
    start()

