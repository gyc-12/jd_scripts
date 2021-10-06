#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jdCookie
活动名称：Env环境-青龙版面CK
Author: SheYu09
'''
import re, os

def Name():
    # 设置被助力的账号可填用户名 或 pin的值不要;
    return ['jd_4fca1d65dfeb3', 'jd_750b7e5869b2b', 'jd_YCayfYCDVacL']

def start():
    if "JD_COOKIE" in os.environ:
        if len(os.environ["JD_COOKIE"]) > 10:
            cookies = os.environ["JD_COOKIE"]
            print()
            print("已获取并使用Env环境 Cookie")                    
    r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
    cookiesList = r.findall(cookies)    
    r = re.compile(r"pt_pin=(.*?);")
    pinNameList = r.findall(cookies)
    if len(cookiesList) > 0 and len(pinNameList) > 0:
        print()
        print("    ********** 您已配置{}个账号 **********".format(len(cookiesList)))
        return cookiesList, pinNameList
    else:
        print("没有可用Cookie，已退出")
        exit(3)
