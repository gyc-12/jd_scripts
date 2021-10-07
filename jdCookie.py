#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jdCookie
活动名称: 拉取青龙版面CK
Author: SheYu09
'''
import requests, re, os

url = ''
client_id = ''
client_secret = ''

# 设置被助力的账号可填用户名 或 pin的值不要;
jd_Name = ['jd_***b3', 'jd_***2b', 'jd_***cL']

def Name():
    if "JD_COOKIE" in os.environ:
        try:
            if len(os.environ["Name"]) > 0:
                Name = os.environ["Name"]
                if '&' in Name:
                    Name = Name.replace('[', '').replace(']', '').replace('\'', '').replace(' ', '').split('&')
                elif ',' in Name:
                    Name = Name.replace('[', '').replace(']', '').replace('\'', '').replace(' ', '').split(',')
                elif '@' in Name:
                    Name = Name.replace('[', '').replace(']', '').replace('\'', '').replace(' ', '').split('@')
                print("已获取并使用Env环境 Name:", Name)
                return Name
        except Exception as e:
            print("自行添加环境变量：Name, 不同好友中间用&符号隔开")
            exit(0)
    else:
        return jd_Name

def getToken(url):
    url += f'/auth/token?client_id={client_id}&client_secret={client_secret}'
    r = requests.get(url=url).json()
    token = r['data']['token']
    token_type = r['data']['token_type']
    expiration = r['data']['expiration']
    return token, token_type, expiration

def getEnv(url, token, token_type, expiration, envStr):
    global cookies
    cookies = ''
    url += f'/envs?searchValue={envStr}&t=expiration'
    headers = {
        "authorization": f"{token_type} {token}"
    }
    r = requests.get(url=url, headers=headers).json()
    data = r['data']
    for i in data:
        cookies += i['value']
    print("  ****** 已获取并使用Client环境 Cookie ******")
    print()
    return cookies

def start():
    if "JD_COOKIE" in os.environ:
        if len(os.environ["JD_COOKIE"]) > 10:
            cookies = os.environ["JD_COOKIE"]
            print("   ****** 已获取并使用Env环境 Cookie ******")
            print()
    else:
        if (url) and (client_id) and (client_secret): 
            token, token_type, expiration = getToken(url)
        else:
            print("自行添加青龙面板: url值, client_id值, client_secret值")
            exit(0)
        cookies = getEnv(url, token, token_type, expiration, 'JD_COOKIE')
    r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
    cookiesList = r.findall(cookies)
    r = re.compile(r"pt_pin=(.*?);")
    pinNameList = r.findall(cookies)
    if len(cookiesList) > 0 and len(pinNameList) > 0:
        print("    ********** 您已配置{}个账号 **********".format(len(cookiesList)))
        print()
        return cookiesList, pinNameList
    else:
        print("没有可用Cookie，已退出")
        print()
        exit(1)
