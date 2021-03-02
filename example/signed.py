# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus 接口调用示例  签约
# date: 2021-02-23

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
signed  Demo:https://www.xxxxx.com/api#signed- 签约
创建 signed 对象，查询 signed 对象，查询 signed 对象列表, 锁定 signed 对象
"""

print("创建签约对象:")
try:

    body = {
    "extra": {},
    "to_wallet": "456489713864648135184651",
    "description": "Option<String>",
    "begin_time": 1613322164,
    "end_time": 1615741364,
    "limit_amount": 456789,
    "day_limit_amount": 147952,
    "month_limit_amount": 585247,
    "total_limit_amount": 82445224
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    signed = yunchaoplus.create_signed(
        request_data = body,
		wallet_id = wallet_id
    )
    print(signed)
except Exception as e:
    print(e)

print("查询签约对象:")
try:
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    signed_id = '28559d5d-1dd2-11b2-802a-6167656e7473'
    signed = yunchaoplus.query_signed(
		wallet_id = wallet_id,
        signed_id = signed_id
    )
    print(signed)
except Exception as e:
    print(e)


print("查询签约对象列表:")
try:
    args = {
    "page": 1,
    "count": 20,
	"begin_time":1613989883,
	"end_time":1619989883
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    signed = yunchaoplus.query_signedlist(
		wallet_id = wallet_id,
        args = args
    )
    print(signed)
except Exception as e:
    print(e)


print("删除签约对象:")
try:

    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    signed_id = '18a3f392-1dd2-11b2-802a-6167656e7473'
    signed = yunchaoplus.delete_signed(
		wallet_id = wallet_id,
        signed_id = signed_id
    )
    print(signed)
except Exception as e:
    print(e)
