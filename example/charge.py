# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus 接口调用示例  支付
# date: 2021-02-22

import sys
import os
import yunchaoplus 

### 初始化
#/////////////////

# 设置 API Key
yunchaoplus.api_key = "123456"

#商家私钥   (绝对路径)
yunchaoplus.skc_path = os.path.join(
    os.path.dirname(__file__), 'Skc')

#商家公钥   (绝对路径)
yunchaoplus.pk0_path = os.path.join(
    os.path.dirname(__file__), 'Pk0.pub')

#平台公钥   (绝对路径)
yunchaoplus.pkc_path = os.path.join(
    os.path.dirname(__file__), 'Pkc.pub')



"""
Charges 支付 Demo:https://www.xxxxx.com/api#charges-支付
创建 charge 对象，查询 charge 对象，查询 charge 对象列表, 撤销 charge 对象
"""

print("创建charge对象:")
try:

    body = {
        "appid": "123456", 
        "channel": "apply",
        "order_no": "147852963258",
        "client_ip": "192.168.1.1",
        "amount": 55828,
        "currency": "YNS",
        "subject": "农产品666",
        "body": "绿色健康无危害teter",
        "time_expire": 457984,
        "description":"无",
        "extra": {}
    }


    dic = {
    "description": "description", 
    "amount": 30,
    "extra": {},
}
 
    args = {
    "page": 1,
    "count": 20
}

    charge = yunchaoplus.create_charge(
        request_data = body
    )
    print(charge)
except Exception as e:
    print(e)

print("查询Charge对象:")
try:
    charge_id = '1aa984f3-1dd2-11b2-802a-7061796d6e74'
    charge = yunchaoplus.query_charge(
        charge_id = charge_id
    )
    print(charge)
except Exception as e:
    print(e)


print("获取Charge对象列表:")
try:
    args = {
    "page": 1,
    "count": 20,
	"begin_time":1613989883,
	"end_time":1619989883
}
    charge = yunchaoplus.query_chargelist(
        args = args
    )
    print(charge)
except Exception as e:
    print(e)


print("撤销Charge对象:")
try:
    charge_id = '2cd393c5-1dd2-11b2-802a-7061796d6e74'
    charge = yunchaoplus.cancel_charge(
        charge_id = charge_id
    )
    print(charge)
except Exception as e:
    print(e)
