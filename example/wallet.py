# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus 接口调用示例  钱包
# date: 2021-02-23

import sys
import os
import yunchaoplus 

#### 初始化
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
wallet 支付 Demo:https://www.xxxxx.com/api#wallets-钱包
创建 wallet 对象，查询 wallet 对象，查询 wallet 对象列表, 锁定 wallet 对象
"""

print("创建钱包对象:")
try:

    body = {
    "encrypted_password":"123456",
    "channel":"22",
    "extra":{"adas":"bbbb"},
    "reviewed":True,
    "block":False
}

    wallet = yunchaoplus.create_wallet(
        request_data = body
    )
    print(wallet)
except Exception as e:
    print(e)

print("查询钱包对象:")
try:
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    wallet = yunchaoplus.query_wallet(
        wallet_id = wallet_id
    )
    print(wallet)
except Exception as e:
    print(e)


print("查询钱包对象列表:")
try:
    args = {
    "page": 1,
    "count": 20,
	"begin_time":1613989883,
	"end_time":1619989883
}
    wallet = yunchaoplus.query_walletlist(
        args = args
    )
    print(wallet)
except Exception as e:
    print(e)


print("锁定钱包对象:")
try:
    lock_dic = {
"block":True
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    wallet = yunchaoplus.lock_wallet(
		request_data = lock_dic,
        wallet_id = wallet_id
    )
    print(wallet)
except Exception as e:
    print(e)


print("通过审核钱包对象:")
try:
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    wallet = yunchaoplus.review_wallet(
        wallet_id = wallet_id
    )
    print(wallet)
except Exception as e:
    print(e)
