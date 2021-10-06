#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / h5st
活动名称: h5st数据加密
Author: SheYu09
'''
import re, random, time, datetime, requests, json, hmac
from urllib.parse import unquote, quote
from hashlib import sha256, sha512, md5

def get_sign(algo, data, key):
    key = key.encode('utf-8')
    message = data.encode('utf-8')
    if algo == 'HmacSHA256':
        algo = sha256
    elif algo == 'HmacSHA512':
        algo = sha512
    elif algo == 'HmacMD5':
        algo = md5
    elif algo == 'SHA256':
        data_sha = sha256(data.encode('utf-8')).hexdigest()
        return data_sha
    elif algo == 'SHA512':
        data_sha = sha512(data.encode('utf-8')).hexdigest()
        return data_sha
    elif algo == 'MD5':
        data_sha = md5(data.encode('utf-8')).hexdigest()
        return data_sha
    else:
        print("加密方式有误！")
        return None
    sign = hmac.new(key, message, digestmod=algo).hexdigest()
    return sign

def stimestamp():
    return round(time.time() * 1000)

def snowtime():
    dateNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return dateNow[:17]

def createFingerprint():
    a = ''.join(random.sample('0123456789578', 13)) + '{}'.format(stimestamp())
    return a[:16]

def requestAlgo(st, appId):
    try:
        fingerprint = createFingerprint()
        timestamp = snowtime()
        iosVer = ''.join(random.sample(["14.5.1", "14.4", "14.3", "14.2", "14.1", "14.0.1", "13.7", "13.1.2", "13.1.1"], 1))
        iosV = iosVer.replace('.', '_')
        url = 'https://cactus.jd.com/request_algo?g_ty=ajax'
        headers = {
            'Authority': 'cactus.jd.com',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'User-Agent': f'Mozilla/5.0 (iPhone; CPU iPhone OS {iosV} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Content-Type': 'application/json',
            'Origin': 'https://st.jingxi.com',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://st.jingxi.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7'
        }
        body = {
                "version": "1.0",
                "fp": '{}'.format(fingerprint),
                "appId": appId,
                "timestamp": stimestamp(),
                "platform": "web",
                "expandParams": ""
        }
        r = requests.post(url, headers=headers, data=json.dumps(body)).json()
        if r['status'] == 200:
            tk = r['data']['result']['tk']
            algo = r['data']['result']['algo']
            digestmod = re.findall(r'algo\.(\w+)\(', algo)
            if len(digestmod) > 0:
                str1 = tk + fingerprint + timestamp + str(appId)
                sign_1 = get_sign(digestmod[0], str1, tk)
                sign_2 = get_sign('HmacSHA256', st, sign_1)
                h5st = f'{timestamp};{fingerprint};{appId};{tk};{sign_2}'
                return quote(h5st)
        else:
            if appId == 10005:
                return '20210608104303790;8489907903583162;10005;tk01w89681aa9a8nZDdIanIyWnVuWFLK4gnqY 05WKcPY3NWU2dcfa73B7PBM7ufJEN0U 4MyHW5N2mT/RNMq72ycJxH;7e6b956f1a8a71b269a0038bbb4abd24bcfb834a88910818cf1bdfc55b7b96e5'
            elif appId == 10010:
                return '20211006165124043;8596757928170419;10010;tk01w078a1e3130ntyNrlshqOpBIKzfCJzC3geuSqd8PZbcjEdhkCKWEqZywtQmfKkguIexXbJEMZnKvtgBV8Shg6ZFd;38151ff3122a1020e3fc5643c4fe0edcdb79e6322582cb5c9aad003c3aa772a5'
            elif appId == 10032:
                return '20211004190341058;6461605528800162;10032;tk01w909b1bfc30ngrf8lTdNIF5711spzYpmP++ILguY4NdGRMM1W2VepYzjX9BoQGq9z05vLpS1nUf8pJzDnoa5HwUv;ca021cc1dc1f513a3f8812fa5bdd76ab2bcad1b129005ecdf8ec336086157420'
    except Exception as e:
        print(e)
        if appId == 10005:
            return '20210608104303790;8489907903583162;10005;tk01w89681aa9a8nZDdIanIyWnVuWFLK4gnqY 05WKcPY3NWU2dcfa73B7PBM7ufJEN0U 4MyHW5N2mT/RNMq72ycJxH;7e6b956f1a8a71b269a0038bbb4abd24bcfb834a88910818cf1bdfc55b7b96e5'
        elif appId == 10010:
            return '20211006171136619;8596757928170419;10010;tk01w078a1e3130ntyNrlshqOpBIKzfCJzC3geuSqd8PZbcjEdhkCKWEqZywtQmfKkguIexXbJEMZnKvtgBV8Shg6ZFd;f68347478ead2f0037e94eda7c2b3b9476bd076a2425f53ed24590ed6e5fb0bf'
        elif appId == 10032:
            return '20211004190341058;6461605528800162;10032;tk01w909b1bfc30ngrf8lTdNIF5711spzYpmP++ILguY4NdGRMM1W2VepYzjX9BoQGq9z05vLpS1nUf8pJzDnoa5HwUv;ca021cc1dc1f513a3f8812fa5bdd76ab2bcad1b129005ecdf8ec336086157420'

def start(url, appId):
    url = unquote(url)
    _stk = re.findall(r'_stk=(.*?)&', url)[0]
    _stklist = _stk.split(',')
    names = locals()
    st = ''
    s = 0
    for i in range(len(_stklist)):
        names[_stklist[i]] = re.findall(r"{0}=(.*?)&".format(_stklist[i]), url)[0]
        if s == len(_stklist)-1:
            st = st + str(_stklist[i]) + ':' + names[_stklist[i]]
        else:
            st = st + str(_stklist[i]) + ':' + names[_stklist[i]] + "&"
        s += 1
    h5st = requestAlgo(st, appId)
    return h5st
