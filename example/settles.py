# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus 接口调用示例  结算
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
settles 支付 Demo:https://www.xxxxx.com/api#settles-结算
创建 settles 对象，查询 settles 对象，查询 settles 对象列表, 删除 settles 对象
"""

print("创建结算对象:")
try:

    body = {
    "channel":"1",
    "recipient":{
        "account":"11",
        "name":"222",
        "open_bank_code":"222",
        "card_type":4
    }
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    settles = yunchaoplus.create_settles(
        request_data = body,
		wallet_id = wallet_id
    )
    print(settles)
except Exception as e:
    print(e)

print("查询结算对象:")
try:
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    settles_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    settles = yunchaoplus.query_settles(
		wallet_id = wallet_id,
        settles_id = settles_id
    )
    print(settles)
except Exception as e:
    print(e)


print("查询结算对象列表:")
try:
    args = {
    "page": 1,
    "count": 20,
	"begin_time":1613989883,
	"end_time":1619989883
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    settles = yunchaoplus.query_settleslist(
		wallet_id = wallet_id,
        args = args
    )
    print(settles)
except Exception as e:
    print(e)


print("删除结算对象:")
try:
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    settles_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    settles = yunchaoplus.delete_settles(
		wallet_id = wallet_id,
        settles_id = settles_id
    )
    print(settles)
except Exception as e:
    print(e)
