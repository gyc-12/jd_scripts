#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / HEADERS
活动名称: headers参数
Author: SheYu09
'''
import USER_AGENTS

def jd_jxcfd(ck):
    headers = {
        "Referer": "https://st.jingxi.com/promote/2021/fortune_island_complex_v2/index.html",
        "Host": "m.jingxi.com",
        "User-Agent": "jdpingou" + USER_AGENTS.userAgent(),
        "Cookie": ck,
    }
    return headers

def jd_jx88hb(ck):
    headers = {
        "Referer": "https://act.jingxi.com/cube/front/activePublish/step_reward/489177.html",
        "Host": "m.jingxi.com",
        "User-Agent": "jdpingou" + USER_AGENTS.userAgent(),
        "Cookie": ck,
    }
    return headers

def jd_jxfhb(ck):
    headers = {
        "Referer": "https://actst.jingxi.com/sns/201907/25/rebate/index.html",
        "Host": "m.jingxi.com",
        "User-Agent": "jdpingou" + USER_AGENTS.userAgent(),
        "Cookie": ck,
    }
    return headers

def jd_fcdyj(ck):
    headers = {
        "Origin": "https://618redpacket.jd.com",
        "Host": "api.m.jd.com",
        "User-Agent": "jdltapp" + USER_AGENTS.userAgent(),
        "Cookie": ck,
    }
    return headers

def jd_tyt(ck):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://pushgold.jd.com",
        "Host": "api.m.jd.com",
        "User-Agent": "jdltapp" + USER_AGENTS.userAgent(),
        "Cookie": ck,
    }
    return headers

def jd_byshf(ck):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://assignment.jd.com/",
        "Host": "api.m.jd.com",
        "User-Agent": "jdltapp" + USER_AGENTS.userAgent(),
        "Cookie": ck,
    }
    return headers



