#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VER 1.0
import requests
import random
import json
import time
ua = [
    'User-Agent,Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'User-Agent,Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
    'User-Agent,Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'User-Agent,Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'User-Agent,Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'User-Agent,Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124'
]  # UA信息来自http://tools.jb51.net/table/useragent，感谢！
base = 'https://api.bilibili.com/x/web-interface/view?'
random.seed(time.time())
s_ua = random.choice(ua)
headers = {
    "User-Agent": s_ua
}


def bvid(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['bvid']


def aid(bvid):
    response = requests.get(url=base+'bvid='+bvid, headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['aid']


def cid(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['cid']


def cover(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['pic']


def view(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['stat']['view']


def video_p(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['videos']


def like(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['stat']['like']


def favorite(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['stat']['favorite']


def danmaku(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['stat']['danmaku']


def coin(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['stat']['coin']


def share(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['stat']['share']


def reply(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['stat']['reply']


def up_name(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['owner']['name']


def up_uid(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['owner']['mid']


def up_face(aid):
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return jdata['data']['owner']['face']


def xml_danmaku_url(aid):
    # 用F12工具箱可以轻松找到弹幕API需要感谢给了我寻找以提醒的【白zz】的【https://blog.csdn.net/u014788374/article/details/80367285】～
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    return 'https://api.bilibili.com/x/v1/dm/list.so?oid='+str(jdata['data']['cid'])


def xml_danmaku_text(aid):
    # 用F12工具箱可以轻松找到弹幕API需要感谢给了我寻找以提醒的【白zz】的【https://blog.csdn.net/u014788374/article/details/80367285】～
    response = requests.get(url=base+'aid='+str(aid), headers=headers)
    jdata = json.loads(response.text)
    response = requests.get(
        url='https://api.bilibili.com/x/v1/dm/list.so?oid='+str(jdata['data']['cid']), headers=headers)
    response.encoding = 'utf-8'
    return response.text
