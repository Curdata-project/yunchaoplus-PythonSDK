# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus 接口调用示例  退款
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
refunds 退款 Demo:https://www.xxxxx.com/api#refunds-退款
创建 refund 对象，查询 refund 对象，查询 refund 对象列表, 撤销 refund 对象
"""

print("创建refund对象:")
try:

	dic = {
    "description": "description", 
    "amount": 1000,
    "extra": {},
}
	charge_id = '2cd393c5-1dd2-11b2-802a-7061796d6e74'
	refund = yunchaoplus.create_refund(
        request_data = dic,
		charge_id = charge_id
    )
	print(refund)
except Exception as e:
	print(e)

print("查询refund对象:")
try:
	refund_id = '27b9f8f1-1dd2-11b2-802a-726566756e64'
	charge_id = '2cd393c5-1dd2-11b2-802a-7061796d6e74'
	refund = yunchaoplus.query_refund(
		charge_id = charge_id,
        refund_id = refund_id
    )
	print(refund)
except Exception as e:
	print(e)


print("获取refund对象列表:")
try:
	args = {
    "page": 1,
    "count": 20,
	"begin_time":1613989883,
	"end_time":1619989883
}
	charge_id = '2cd393c5-1dd2-11b2-802a-7061796d6e74'
	refund = yunchaoplus.query_refundlist(
		charge_id = charge_id,
        args = args
		)
	print(refund)
except Exception as e:
	print(e)


