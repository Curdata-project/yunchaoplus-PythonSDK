# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus钱包
# date: 2021-02-19


import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
sys.path.append(BASE_DIR)


from tools.send import yunchaoplusRequestObject,GET_yunchaoplusRequestObject
from os import urandom
from base64 import b64encode
from settings import *
import yunchaoplus

def create_wallet(request_data):
	obj = yixuan_yunchaoplus_wallet(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.create_wallet_obj(request_data)
	return example

def lock_wallet(request_data,wallet_id):
	obj = yixuan_yunchaoplus_wallet(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.lock_wallet_obj(request_data,wallet_id)
	return example

def create_settles(request_data,wallet_id):
	obj = yixuan_yunchaoplus_wallet(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.create_settles_obj(request_data,wallet_id)
	return example

#通过审核钱包
def review_wallet(wallet_id):
	obj = yixuan_yunchaoplus_wallet_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.review_wallet_obj(wallet_id)
	return example

def query_wallet(wallet_id):
	obj = yixuan_yunchaoplus_wallet_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_wallet_obj(wallet_id)
	return example

def query_walletlist(args):
	obj = yixuan_yunchaoplus_wallet_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_wallet_objlist(args)
	return example

def query_settles(wallet_id,settles_id):
	obj = yixuan_yunchaoplus_wallet_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_settles_obj(wallet_id,settles_id)
	return example

def query_settleslist(wallet_id,args):
	obj = yixuan_yunchaoplus_wallet_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_settles_objlist(wallet_id,args)
	return example

def delete_settles(wallet_id,settles_id):
	obj = yixuan_yunchaoplus_wallet_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.delete_settles_obj(wallet_id,settles_id)
	return example


class yixuan_yunchaoplus_wallet(yunchaoplusRequestObject):

	#创建钱包对象
	def create_wallet_obj(self,request_data):
		return self.send(request_data, 'POST', 'https://%s/wallets'%WALLET_DNS)

	#锁定钱包对象 PUT $endpoint/wallets/${id}/block
	def lock_wallet_obj(self, request_data, wallet_id):
		return self.send(request_data, 'PUT', 'https:/%s/wallets/%s/block' % (WALLET_DNS,wallet_id))

	#创建结算对象  POST $endpoint/wallets/${wallet_id}/settles
	def create_settles_obj(self, request_data, wallet_id):
		return self.send(request_data, 'POST', 'https://%s/wallets/%s/settles' % (WALLET_DNS, wallet_id))


class yixuan_yunchaoplus_wallet_2(GET_yunchaoplusRequestObject):
	
	#通过审核钱包对象 PUT $endpoint/wallets/${id}/review
	def review_wallet_obj(self, wallet_id):
		return self.send('PUT', 'https://%s/wallets/%s/review' % (WALLET_DNS,wallet_id))

	#查询钱包对象 GET $endpoint/wallets/{id}
	def query_wallet_obj(self,wallet_id):
		return self.send('GET', 'https://%s/wallets/%s' % (WALLET_DNS,wallet_id))
	
	#查询钱包对象列表 GET $endpoint/wallets   ###count=2&page=0&begin_time=1613227719&end_time=1613227719
	def query_wallet_objlist(self,args):
		url = 'https://%s/wallets?count=%s&page=%s' % (WALLET_DNS,args.get('count'),args.get('page'))
		if args.get('begin_time'):
			url = 'https://%s/wallets/%s/?count=%s&page=%s&begin_time=%s&end_time=%s' % (WALLET_DNS,wallet_id,
			   args.get('count'),args.get('page'),args.get('begin_time'),args.get('end_time'))
		print('查询钱包对象列表url:', url)
		return self.send('GET', url)

	#查询结算对象  GET $endpoint/wallets/{wallet_id}/settles/${id}
	def query_settles_obj(self, wallet_id, id):
		return self.send('GET', 'https://%s/wallets/%s/settles/%s' % (WALLET_DNS,wallet_id,id))

	#查询结算对象列表  GET $endpoint/wallets/${wallet_id}/settles   count=1&page=0&begin_time=1613231083&end_time=1613231083
	def query_settles_objlist(self, wallet_id, args):
		url = 'https://%s/wallets/%s/settles?count=%s&page=%s' % (WALLET_DNS,wallet_id,args.get('count'),args.get('page'))
		if args.get('begin_time'):
			url = 'https://%s/wallets/%s/settles?count=%s&page=%s&begin_time=%s&end_time=%s' % (WALLET_DNS,wallet_id,
			   args.get('count'),args.get('page'),args.get('begin_time'),args.get('end_time'))
		print('查询结算对象列表url:', url)
		return self.send('GET', url)

	#删除结算对象  DELETE $endpoint/wallets/{wallet_id}/settles/${id}
	def delete_settles_obj(self, wallet_id, id):
		return self.send('DELETE', 'https://%s/wallets/%s/settles/%s' % (WALLET_DNS,wallet_id,id))
