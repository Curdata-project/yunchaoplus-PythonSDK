# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus充值 和 提现
# date: 2021-02-20



import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
sys.path.append(BASE_DIR)


from tools.send import yunchaoplusRequestObject,GET_yunchaoplusRequestObject
from os import urandom
from base64 import b64encode
from settings import *
import yunchaoplus

def create_withdraw(request_data,wallet_id):
	obj = yixuan_yunchaoplus_withdraw(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.create_withdraw_obj(request_data,wallet_id)
	return example

def update_withdraw(request_data,wallet_id,withdraw_id):
	obj = yixuan_yunchaoplus_withdraw(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.update_withdraw_obj(request_data,wallet_id,withdraw_id)
	return example

def create_recharge(request_data,wallet_id):
	obj = yixuan_yunchaoplus_withdraw(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.create_recharge_obj(request_data,wallet_id)
	return example

def query_withdraw(wallet_id,withdraw_id):
	obj = yixuan_yunchaoplus_withdraw_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_withdraw_obj(wallet_id,withdraw_id)
	return example

def query_withdrawlist(wallet_id, args):
	obj = yixuan_yunchaoplus_withdraw_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_withdraw_objlist(wallet_id, args)
	return example

def query_recharge(wallet_id,recharge_id):
	obj = yixuan_yunchaoplus_withdraw_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_recharge_obj(wallet_id,recharge_id)
	return example

def query_rechargelist(wallet_id,args):
	obj = yixuan_yunchaoplus_withdraw_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_recharge_objlist(wallet_id,args)
	return example



class yixuan_yunchaoplus_withdraw(yunchaoplusRequestObject):

	#创建提现对象  POST $endpoint/wallets/${wallet_id}/withdraws
	def create_withdraw_obj(self,request_data,wallet_id):
		url = 'https://%s/wallets/%s/withdraws'% (WITHDRAW_DNS,wallet_id)
		print('创建提现对象url:', url)
		return self.send(request_data, 'POST', url)
	
	#更新提现对象  PUT $endpoint/wallets/${wallet_id}/withdraws/${id}
	def update_withdraw_obj(self,request_data,wallet_id,id):
		return self.send(request_data, 'PUT', 'https://%s/wallets/%s/withdraws/%s'% (WITHDRAW_DNS,wallet_id,id))

	#创建充值对象   POST $endpoint/wallets/${wallet_id}/recharges
	def create_recharge_obj(self,request_data,wallet_id):
		return self.send(request_data, 'POST', 'https://%s/wallets/%s/recharges'% (WITHDRAW_DNS,wallet_id))


class yixuan_yunchaoplus_withdraw_2(GET_yunchaoplusRequestObject):

	#查询提现对象  GET $endpoint/wallets/${wallet_id}/withdraws/${id}
	def query_withdraw_obj(self,wallet_id, id):
		return self.send('GET', 'https://%s/wallets/%s/withdraws/%s' % (WITHDRAW_DNS,wallet_id,id))

	#查询提现对象列表   GET $endpoint/wallets/${wallet_id}/withdraws
	def query_withdraw_objlist(self, wallet_id, args):
		url = 'https://%s/wallets/%s/withdraws?count=%s&page=%s' % (WITHDRAW_DNS,wallet_id,args.get('count'),args.get('page'))
		if args.get('created_begin'):
			url = 'https://%s/wallets/%s/withdraws?count=%s&page=%s&created_begin=%s&created_end=%s' % (WITHDRAW_DNS,wallet_id,
			   args.get('count'),args.get('page'),args.get('created_begin'),args.get('created_end'))
		print('查询提现对象列表url:', url)
		return self.send('GET', url)	

	#查询充值对象  GET $endpoint/wallets/${wallet_id}/recharges/${id}
	def query_recharge_obj(self,wallet_id, id):
		return self.send('GET', 'https://%s/wallets/%s/recharges/%s' % (WITHDRAW_DNS,wallet_id,id))

	#查询充值对象列表   GET $endpoint/wallets/${wallet_id}/recharges
	def query_recharge_objlist(self, wallet_id, args):
		url = 'https://%s/wallets/%s/recharges?count=%s&page=%s' % (WITHDRAW_DNS,wallet_id,args.get('count'),args.get('page'))
		if args.get('created_begin'):
			url = 'https://%s/wallets/%s/recharges?count=%s&page=%s&created_begin=%s&created_end=%s' % (WITHDRAW_DNS,wallet_id,
			   args.get('count'),args.get('page'),args.get('created_begin'),args.get('created_end'))
		print('查询充值对象列表url:', url)
		return self.send('GET', url)	
