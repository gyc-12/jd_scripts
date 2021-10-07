#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_fcdyj_wxtx
活动名称: 发财大赢家-微信提现-助力
Author: SheYu09
'''
import jdCookie, HEADERS, posturl, requests, json, time

def getShareCode(purl, bodys1, bodys2, header):
    try:
        url = f'{purl}redEnvelopeInteractHome{bodys1}{bodys2}'
        r = requests.get(url=url, headers=header, timeout=30).text
        data = json.loads(r)
        if data['data']['checkResult']['errMsg'] == '助力失败':
            redEnvelopeId = data["data"]["redEnvelopeId"]
            markedPin = data["data"]["markedPin"]
            aNum = 0
            # print(redEnvelopeId, markedPin)
            return redEnvelopeId, markedPin
        else:
            print("获取互助码失败！")
            print()
            return 0, 0
    except Exception as e:
        if aNum < 5:
            aNum += 1
            return getShareCode(purl, bodys1, bodys2, header)
        else:
            aNum = 0
            print("获取互助码失败！", e)
            print()
            return 0, 0

def helpCode(purl, bodys1, bodys2, header, redEnvelopeId, inviter, uNUm, user):
    print(f'====用户{uNUm} {user} 助力====')
    print()
    try:
        url = f'{purl}openRedEnvelopeInteract{bodys1},"redEnvelopeId":"{redEnvelopeId}","inviter":"{inviter}","helpType":"2"{bodys2}'
        r = requests.get(url=url, headers=header, timeout=30).text
        data = json.loads(r)
        code = data["data"]["helpResult"]['code']
        print(data)
        if code == 0:
            print(f'{data["data"]["helpResult"]["errMsg"]}')
            print(f'获得{data["data"]["helpResult"]["data"]["amount"]}红包')
        else:
            if code == 16018:
                print('你的好友今日还未获得奖励')
                print('提现助力失败')
            else:
                print(f'{data["data"]["helpResult"]["errMsg"]}')
        print()
        return code
    except Exception as e:
        print("helpCode Error", e)
        print('报错了！')
        print()

def exchange(purl, bodys1, bodys2, header):
    print(f"****【京东账号】{pinNameList[int(ckNum)]} 开始提现 ****")
    print()
    try:
        url = f'{purl}exchange{bodys1},"rewardType":2{bodys2}'
        r = requests.get(url=url, headers=header, timeout=30).text
        data = json.loads(r)
        if data['code'] == 0:
            print(f'{data["errMsg"]}')
            print(f'提现金额: {data["data"]["chatEnvelopeVo"]["rewardValue"]}元')
            print(f'{data["data"]["chatEnvelopeVo"]["message"]}')
        else:
            print(f'{data["errMsg"]}')
        print()
    except Exception as e:
        print("helpCode Error", e)
        print('报错了！')
        print()

def start(ck):
    print('    ******* 发财大赢家-微信提现-助力 *******')
    print()
    cookiesList, pinNameList = jdCookie.start()
    for ckname in [f'{ck}']:
        try:
            ckNum = pinNameList.index(ckname)
        except:
            print(f"请检查被助力账号【{ckname}】名称是否正确？提示：助力名字可填pt_pin的值、也可以填账号名。")
            print()
            continue
        print(f"*******开始【京东账号】{pinNameList[int(ckNum)]} *******")
        print()
        purl, body1, body2 = posturl.jd_fcdyj()
        redEnvelopeId, markedPin = getShareCode(purl, body1, body2, HEADERS.jd_fcdyj(cookiesList[ckNum]))
        if redEnvelopeId == 0:
            print(f"===【京东账号】{pinNameList[int(ckNum)]}  获取互助码失败。请稍后再试！==")
            print()
            continue
        u = 0
        for i in cookiesList:
            if i == cookiesList[ckNum]:
                u += 1
                continue
            code = helpCode(purl, body1, body2, HEADERS.jd_fcdyj(i), redEnvelopeId, markedPin, u+1, pinNameList[u])
            print()
            if code == 16005:
                exchange(purl, body1, body2, HEADERS.jd_fcdyj(cookiesList[ckNum]))
                break
            elif code == 16011:
                break
            elif code == 16018:
                break
            time.sleep(1)
            u += 1

aNum = 0

