# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus 接口调用示例  提现
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
withdraw 支付 Demo:https://www.xxxxx.com/api#withdraw- 提现
创建 withdraw 对象，查询 withdraw 对象，查询 withdraw 对象列表, 锁定 withdraw 对象
"""

print("创建提现对象:")
try:

    body = {
  "amount": 100,
  "settle": "b367370f-de92-4efa-a427-0845054035f5",
  "description": "optional description",
  "extra": {
  }
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    withdraw = yunchaoplus.create_withdraw(
        request_data = body,
		wallet_id = wallet_id
    )
    print(withdraw)
except Exception as e:
    print(e)

print("查询提现对象:")
try:
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    withdraw_id = '57d8609e-27be-4529-a931-c32b858be98e'
    withdraw = yunchaoplus.query_withdraw(
		wallet_id = wallet_id,
        withdraw_id = withdraw_id
    )
    print(withdraw)
except Exception as e:
    print(e)


print("查询提现对象列表:")
try:
    args = {
    "page": 1,
    "count": 20,
	"begin_time":1613989883,
	"end_time":1619989883
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    withdraw = yunchaoplus.query_withdrawlist(
		wallet_id = wallet_id,
        args = args
    )
    print(withdraw)
except Exception as e:
    print(e)


print("更新提现对象:")
try:
    body = {
  "status": "pending"
}
    wallet_id = 'c3d4c64f-26ea-49ea-9629-791c18f9abbf'
    withdraw_id = '57d8609e-27be-4529-a931-c32b858be98e'
    withdraw = yunchaoplus.update_withdraw(
		request_data = body,
		wallet_id = wallet_id,
        withdraw_id = withdraw_id
    )
    print(withdraw)
except Exception as e:
    print(e)
