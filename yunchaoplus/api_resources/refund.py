# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus退款
# date: 2021-02-22

import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
sys.path.append(BASE_DIR)


from tools.send import yunchaoplusRequestObject,GET_yunchaoplusRequestObject
from os import urandom
from base64 import b64encode
from settings import *
import yunchaoplus 

def create_refund(request_data,charge_id):
	obj = yixuan_yunchaoplus_refund(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.create_refund_obj(request_data,charge_id)
	return example

def query_refund(charge_id,refund_id):
	obj = yixuan_yunchaoplus_refund_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_refund_obj(charge_id,refund_id)
	return example

def query_refundlist(charge_id,args):
	obj = yixuan_yunchaoplus_refund_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_refund_objlist(charge_id,args)
	return example


class yixuan_yunchaoplus_refund(yunchaoplusRequestObject):

	#创建退款对象 POST $endpoint/charges/{id}/refunds
	def create_refund_obj(self,request_data, charge_id):
		url = 'https://%s/charges/%s/refunds' % (REFUND_DNS,charge_id)
		print('创建退款对象url:', url)
		return self.send(request_data, 'POST', url)



class yixuan_yunchaoplus_refund_2(GET_yunchaoplusRequestObject):
	
	#查询退款对象 GET $endpoint/charges/{charge_id}/refunds/{refund_id}
	def query_refund_obj(self, charge_id, refund_id):
		url = 'https://%s/charges/%s/refunds/%s' % (REFUND_DNS, charge_id, refund_id)
		print('查询退款对象:', url)
		return self.send('GET', url)

	#查询退款对象列表 GET $endpoint/charges/{id}/refunds
	def query_refund_objlist(self, charge_id, args):
		url = 'https://%s/charges/%s/refunds?page=%s&count=%s' % (REFUND_DNS, charge_id,args.get('page'), args.get('count'))
		print('查询退款对象列表：', url)
		if args.get('begin_time'):
			url = 'https://%s/charges/%s/refunds?page=%s&count=%s&begin_time=%s&end_time=%s' % (REFUND_DNS, 
				charge_id,args.get('page'), args.get('count'),args.get('begin_time'),args.get('end_time'))	
		return self.send('GET', url)


