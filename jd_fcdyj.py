#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_fcdyj
活动名称: 发财大赢家-拆红包-助力
Author: SheYu09
cron: 0 0 * * * jd_fcdyj.py
new Env('极速版 -*- 发财大赢家')
'''
import jdCookie, HEADERS, posturl, jd_fcdyj_wxtx, requests, json, time

aNum = 0
def getShareCode(purl, bodys1, bodys2, header):
    global aNum
    try:
        url = f'{purl}openRedEnvelopeInteract{bodys1}{bodys2}'
        r = requests.get(url=url, headers=header, timeout=30).text
        data = json.loads(r)
        amount = data["data"]["amount"]
        if data["data"]["needAmount"] == "0" and data["data"]["amountEnough"] == True:
            return 1, 1, amount
        elif data["data"]["needAmount"] != "0" and data["data"]["amountEnough"] == False:
            url1 = f'{purl}redEnvelopeInteractHome{bodys1}{bodys2}'
            r1 = requests.get(url=url1, headers=header, timeout=30).text
            data1 = json.loads(r1)
            if data1['data']['checkResult']['errMsg'] == '助力失败':
                redEnvelopeId = data1["data"]["redEnvelopeId"]
                #code = data1["data"]["checkResult"]["code"]
                markedPin = data1["data"]["markedPin"]
                return redEnvelopeId, markedPin, amount
    except Exception as e:
        if aNum < 5:
            aNum += 1
            return getShareCode(purl, bodys1, bodys2, header)
        else:
            aNum = 0
            print(f'========== 【京东账号】{pinNameList[int(ckNum)]} 已被Jd拉黑 ==========')
            print()
            return 3, 3, 3

def helpCode(purl, bodys1, bodys2, header, redEnvelopeId, inviter, uNUm, user, name):
    print(f'====用户{uNUm} {user} 助力====')
    try:
        url = f'{purl}openRedEnvelopeInteract{bodys1},"redEnvelopeId":"{redEnvelopeId}","inviter":"{inviter}","helpType":"1"{bodys2}'
        r = requests.get(url=url, headers=header, timeout=30).text
        data = json.loads(r)
        code = data["data"]["helpResult"]['code']
        # print(data)
        if code == 0:
            print()
            print(f'{data["data"]["helpResult"]["errMsg"]}')
            print(f'获得{data["data"]["helpResult"]["data"]["amount"]}红包')
        else:
            if code == 16018:
                print()
                print('你的好友今日还未获得奖励')
                print('提现助力失败')
            else:
                print()
                print(f'{data["data"]["helpResult"]["errMsg"]}')
        return code
    except Exception as e:
        print()
        print("helpCode Error", e)
        print('报错了！')

def start():
    global cookiesList, pinNameList, ckNum
    print('    ******* 发财大赢家-拆红包-助力 *******')
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
        purl, body1, body2 = posturl.jd_fcdyj()
        redEnvelopeId, markedPin, amount = getShareCode(purl, body1, body2, HEADERS.jd_fcdyj(cookiesList[ckNum]))
        if redEnvelopeId == 0:
            print(f"===【京东账号】{pinNameList[int(ckNum)]}  获取互助码失败。请稍后再试！==")
            print()
            time.sleep(0.1)
            continue
        elif redEnvelopeId == 1:
            print(f"==========【京东账号】{pinNameList[int(ckNum)]} 已提现: {amount}元==========")
            print()
            time.sleep(0.1)
            continue
        elif redEnvelopeId == 3:
            time.sleep(0.1)
            continue
        u = 0
        for i in cookiesList:
            if i == cookiesList[ckNum]:
                u += 1
                continue
            code = helpCode(purl, body1, body2, HEADERS.jd_fcdyj(i), redEnvelopeId, markedPin, u+1, pinNameList[u], pinNameList[ckNum])
            print()
            time.sleep(0.1)
            u += 1
        jd_fcdyj_wxtx.start(ckname)
  
if __name__ == '__main__':
    start()
