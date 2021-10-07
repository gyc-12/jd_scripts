#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_jxcfd
活动名称: 财富岛-合成珍珠红包-助力
Author: SheYu09
cron: 0 0 * * * jd_jxcfd.py
new Env('京喜 -*- 财富岛红包')
'''
import jdCookie, HEADERS, h5st, posturl, jd_jxcfd_hb, requests, json, time

def getShareCode(purl, bodys, header):
    try:
        url = f'{purl}user/ComposePearlState{bodys}'
        r = requests.get(url=url, headers=header).text
        data = json.loads(r)
        return data["strMyShareId"]
    except Exception as e:
        if aNum < 5:
            aNum += 1
            return getShareCode(purl, bodys, header)
        else:
            aNum = 0
            print("获取互助码失败！", e)
            print()
            return 0

def helpCode(purl, bodys, header, strMyShareId, uNUm, user):
    print(f'====用户{uNUm} {user} 助力====')
    print()
    try:
        url = f'{purl}user/PearlHelpByStage{bodys}&strShareId={strMyShareId}&_stk=strShareId%2CstrZone&h5st='
        url += h5st.start(url, '10032')
        r = requests.get(url=url, headers=header).text
        data = json.loads(r)
        url = f'{purl}story/helpbystage{bodys}&strShareId={strMyShareId}&_stk=strShareId%2CstrZone&h5st='
        url += h5st.start(url, '10032')
        r = requests.get(url=url, headers=header).text
        data1 = json.loads(r)
        iRet = data["iRet"]
        if data["iRet"] == 0 and data1["iRet"] == 0:
            print(f'{data1["sErrMsg"]}')
            print(f'获得: {data["GuestPrizeInfo"]["strPrizeName"]}')
            print(f'{data1["Data"]["AppHbInfo"]["strContent"]}')
            print(f'获得: {data1["Data"]["AppHbInfo"]["GuestPrizeInfo"]["strPrizeName"]}')
        else:
            print(f'{data["sErrMsg"]}')
            print(f'{data1["sErrMsg"]}')
        print()
        return iRet
    except Exception as e:
        print("helpCode Error", e)
        print('报错了！')
        print()

def start():
    jd_jxcfd_hb.start()
    print('    ******* 财富大陆-合成珍珠红包-助力 *******')
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
        purl, body = posturl.jd_jxcfd()
        strMyShareId = getShareCode(purl, body, HEADERS.jd_jxcfd(cookiesList[ckNum]))
        if strMyShareId == 0:
            print(f"===【京东账号】{pinNameList[int(ckNum)]}  获取互助码失败。请稍后再试！==")
            print()
            continue
        u = 0
        for i in cookiesList:
            if i == cookiesList[ckNum]:
                u += 1
                continue
            iRet = helpCode(purl, body, HEADERS.jd_jxcfd(i), strMyShareId, u+1, pinNameList[u])
            print()
            if iRet == 2190:
                break
            time.sleep(0.01)
            u += 1

aNum = 0
if __name__ == '__main__':
    start()

