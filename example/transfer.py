# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus 接口调用示例  转账
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
transfers 转账 Demo:https://www.xxxxx.com/api#transfers-转账
创建 transfer 对象，查询 transfer 对象，查询 transfer 对象列表, 撤销 transfer 对象
"""

print("创建transfer对象:")
try:

	body = {
    "extra": {},
    "to_wallet": "54564813484135515",
    "description": "测试创建一个交易数据"
}
	wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
	transfer = yunchaoplus.create_transfer(
        request_data = body,
		wallet_id = wallet_id
    )
	print(transfer)
except Exception as e:
	print(e)

print("查询transfer对象:")
try:
	wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
	transfer_id = '195871b5-1dd2-11b2-802a-7472616e7366'
	transfer = yunchaoplus.query_transfer(
		wallet_id = wallet_id,
        transfer_id = transfer_id
    )
	print(transfer)
except Exception as e:
	print(e)


print("获取transfer对象列表:")
try:
	args = {
    "page": 1,
    "count": 20,
	"begin_time":1613989883,
	"end_time":1619989883
}
	wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
	transfer = yunchaoplus.query_transferlist(
		wallet_id = wallet_id,
        args = args
		)
	print(transfer)
except Exception as e:
	print(e)
