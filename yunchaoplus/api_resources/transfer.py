# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus转账
# date: 2021-02-20

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
sys.path.append(BASE_DIR)


from tools.send import yunchaoplusRequestObject,yixuan_yunchaoplusRequestObject
from os import urandom
from base64 import b64encode
from settings import *
import yunchaoplus 

def create_transfer(request_data,wallet_id):
	obj = yixuan_yunchaoplus_transfer(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.create_transfer_obj(request_data,wallet_id)
	return example

def query_transfer(wallet_id,transfer_id):
	obj = yixuan_yunchaoplus_transfer_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_transfer_obj(wallet_id,transfer_id)
	return example

def query_transferlist(wallet_id,args):
	obj = yixuan_yunchaoplus_transfer_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_transfer_objlist(wallet_id,args)
	return example

def update_transfer(request_data,wallet_id,transfer_id):
	obj = yixuan_yunchaoplus_transfer(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.update_transfer_obj(request_data,wallet_id,transfer_id)
	return example


class yixuan_yunchaoplus_transfer(yunchaoplusRequestObject):
	def __init__(self, api_key, pk0_path, pkc_path, skc_path):
		yunchaoplusRequestObject.__init__(self, api_key, pk0_path, pkc_path, skc_path)

	#创建转账对象 POST $endpoint/wallets/${wallet_id}/transfers
	def create_transfer_obj(self,request_data,wallet_id):
		return self.send(request_data, 'POST', 'https://%s/wallets/%s/transfers'% (TRANSFER_DNS,wallet_id))
	
	#更新转账对象  PUT $endpoint/transfers/${wallet_id}/transfers/${id}
	def update_transfer_obj(self,request_data,wallet_id,id):
		return self.send(request_data, 'PUT', 'https://%s/transfers/%s/transfers/%s'% (TRANSFER_DNS,wallet_id,id))



class yixuan_yunchaoplus_transfer_2(yixuan_yunchaoplusRequestObject):
	def __init__(self, api_key, pk0_path, pkc_path, skc_path):
		yunchaoplusRequestObject.__init__(self, api_key, pk0_path, pkc_path, skc_path)

	#查询转账对象  GET $endpoint/wallets/${wallet_id}/transfers/${id}
	def query_transfer_obj(self,wallet_id, id):
		url = 'https://%s/wallets/%s/transfers/%s' % (TRANSFER_DNS,wallet_id,id)
		print('查询转账对象:',url)
		return self.send('GET', url)

	#查询转账对象列表   POST $endpoint/wallets/${wallet_id}/transfers
	def query_transfer_objlist(self, wallet_id, args):
		url = 'https://%s/wallets/%s/transfers?count=%s&page=%s' % (TRANSFER_DNS,wallet_id,args.get('count'),args.get('page'))
		if args.get('begin_time'):
			url = 'https://%s/wallets/%s/transfers?count=%s&page=%s&begin_time=%s&end_time=%s' % (TRANSFER_DNS,wallet_id,
			   args.get('count'),args.get('page'),args.get('begin_time'),args.get('end_time'))
		print('查询转账对象列表url:', url)
		return self.send('GET', url)	
