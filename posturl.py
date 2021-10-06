#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / posturl
活动名称: 链接地址-变量
Author: SheYu09
'''

def jdltapp():
    return 'https://api.m.jd.com/'

def jd_jxcfd():
    url = 'https://m.jingxi.com/jxbfd/'
    body = '?strZone=jxbfd&sceneval=2'
    return url, body

def jd_jx88hb():
    url = 'https://m.jingxi.com/cubeactive/steprewardv3/'
    body = '?activeId=489177&channel=7&sceneval=2&_stk=activeId'
    return url, body

def jd_fcdyj():
    url = 'https://api.m.jd.com/?functionId='
    body1 = '&body={"linkId":"yMVR-_QKRd2Mq27xguJG-w"'
    body2 = '}&appid=activities_platform&client=H5&clientVersion=1.0.0'
    return url, body1, body2

def jd_tyt():
    url = 'https://api.m.jd.com/'
    body1 = '&body={"actId":"287eb90945e049129d76dd7e85dc0313","channel":"coin_dozer"'
    body2 = '}&appid='
    return url, body1, body2

def jd_byshf():
    url = 'https://api.m.jd.com/'
    body1 = 'functionId=TaskInviteService&body={"method":"'
    body2 = '","data":{"channel":"1"'
    body3 = '}}&appid=market-task-h5'
    return url, body1, body2, body3



