# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus 接口调用示例  充值
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
recharge 支付 Demo:https://www.xxxxx.com/api#recharge-充值
创建 recharge 对象，查询 recharge 对象，查询 recharge 对象列表, 更新 recharge 对象
"""

print("创建充值对象:")
try:

    body = {
  "recharge_amount": 100,
  "settle": "f0c3399f-1cce-4b6c-8d5a-5f698c91ff89",
  "description": "optional description",
  "extra": {
  }
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    recharge = yunchaoplus.create_recharge(
        request_data = body,
		wallet_id = wallet_id
    )
    print(recharge)
except Exception as e:
    print(e)

print("查询充值对象:")
try:
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    recharge_id = '21fd5590-74b2-4a0b-bd41-153d121f4af2'
    recharge = yunchaoplus.query_recharge(
		wallet_id = wallet_id,
        recharge_id = recharge_id
    )
    print(recharge)
except Exception as e:
    print(e)


print("查询充值对象列表:")
try:
    args = {
    "page": 1,
    "count": 20,
	"begin_time":1613989883,
	"end_time":1619989883
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    recharge = yunchaoplus.query_rechargelist(
		wallet_id = wallet_id,
        args = args
    )
    print(recharge)
except Exception as e:
    print(e)

