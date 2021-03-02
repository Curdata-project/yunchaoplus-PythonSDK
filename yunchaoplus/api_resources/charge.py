
# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus支付
# date: 2021-02-19

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
sys.path.append(BASE_DIR)

from ..tools.send import *
from os import urandom
from base64 import b64encode
from settings import *
import yunchaoplus


def create_charge(request_data):
	print('api_resources 创建支付对象:',request_data)
	print('api_key:',yunchaoplus.api_key)
	obj = yixuan_yunchaoplus_charge(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.create_charge_obj(request_data)
	return example

def query_charge(charge_id):
	obj = yixuan_yunchaoplus_charge_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_charge_obj(charge_id)
	return example

def query_chargelist(args):
	obj = yixuan_yunchaoplus_charge_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_charge_objlist(args)
	return example

def cancel_charge(charge_id):
	obj = yixuan_yunchaoplus_charge_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.cancel_charge_obj(charge_id)
	return example
		

class yixuan_yunchaoplus_charge(yunchaoplusRequestObject):
	def __init__(self, api_key, pk0_path, pkc_path, skc_path):
		yunchaoplusRequestObject.__init__(self, api_key, pk0_path, pkc_path, skc_path)

	#创建支付对象
	def create_charge_obj(self,request_data):
		url = 'https://%s/charges'%CHARGE_DNS
		print('创建支付对象url:',url)
		# example = yixuan_yunchaoplus(self.api_key, self.pk0_path, self.pkc_path, self.skc_path)
		return self.send(request_data, 'POST',url)


class yixuan_yunchaoplus_charge_2(yixuan_yunchaoplusRequestObject):
	def __init__(self, api_key, pk0_path, pkc_path, skc_path):
		yunchaoplusRequestObject.__init__(self, api_key, pk0_path, pkc_path, skc_path)

	#撤销支付对象
	def cancel_charge_obj(self, charge_id):
		return self.send('DELETE', 'https://%s/charges/%s' % (CHARGE_DNS,charge_id))
	
	#查询支付对象
	def query_charge_obj(self, charge_id):
		return self.send('GET', 'https://%s/charges/%s' % (CHARGE_DNS,charge_id))

	#查询支付对象列表 GET $endpoint/charges  http://127.0.0.1:9010/charges?page=1&count=10
	def query_charge_objlist(self, args):
		url = 'https://%s/charges?page=%s&count=%s' % (CHARGE_DNS, args.get('page'), args.get('count'))
		print('查询支付对象列表url:', url)
		return self.send('GET',url)

