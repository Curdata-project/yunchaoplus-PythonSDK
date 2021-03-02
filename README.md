# yunchaoplus Python SDK
---

## 简介

此SDK包兼容windows（32位）（64位）,linux （32位）（64位） 的 python2,python3 版本,且向下兼容（64位系统可装32位python）

yunchaoplus 文件夹下是 Python SDK 文件，
example 文件夹里面是简单的接入示例，该示例仅供参考。

## 安装

使用 setup.py 手动安装  

注意：执行安装文件之前需要安装pip工具,并升级至最新版本,执行 sudo pip install pyOpenSSL

```
python setup.py install
```

## 接入方法
[示例代码](example/)

### 初始化

 * 设置 API Key
```python
yunchaoplus.api_key = "your api_key"
```

 * 商家私钥   (绝对路径)
 ```python
yunchaoplus.skc_path = os.path.join(
	os.path.dirname(__file__), 'your private key file name')
```

 * 商家公钥   (绝对路径)
 ```python
yunchaoplus.pk0_path = os.path.join(
	os.path.dirname(__file__), 'your public key file name')
```

 * 平台公钥   (绝对路径)
 ```python
yunchaoplus.pkc_path = os.path.join(
	os.path.dirname(__file__), 'curdata public key file name')
```



###	Charges 支付 
	
	创建 charge 对象，查询 charge 对象，查询 charge 对象列表, 撤销 charge 对象
	
```python
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
```


### recharge 充值

	创建 recharge 对象，查询 recharge 对象，查询 recharge 对象列表, 更新 recharge 对象

```python
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
```


### refunds 退款

	创建 refund 对象，查询 refund 对象，查询 refund 对象列表, 撤销 refund 对象

```python
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
```


###	settles 结算

	创建 settles 对象，查询 settles 对象，查询 settles 对象列表, 删除 settles 对象

```python
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
```


###	signed 签约

	创建 signed 对象，查询 signed 对象，查询 signed 对象列表, 锁定 signed 对象

```python
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
```


###	transfers 转账

	创建 transfer 对象，查询 transfer 对象，查询 transfer 对象列表, 撤销 transfer 对象

```python
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
```


###	wallet 钱包

	创建 wallet 对象，查询 wallet 对象，查询 wallet 对象列表, 锁定 wallet 对象

```python
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
```


###	withdraw 提现

	创建 withdraw 对象，查询 withdraw 对象，查询 withdraw 对象列表, 锁定 withdraw 对象

```python
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
```
