# -*- coding: utf-8 -*-
# author: 逸轩
# desc: 云钞plus签约
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

def create_signed(request_data,wallet_id):
	obj = yixuan_yunchaoplus_agent(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.create_agent_obj(request_data,wallet_id)
	return example

def delete_signed(wallet_id,signed_id):
	obj = yixuan_yunchaoplus_agent_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.delete_agent_obj(wallet_id,signed_id)
	return example


def query_signed(wallet_id,signed_id):
	obj = yixuan_yunchaoplus_agent_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_agent_obj(wallet_id,signed_id)
	return example

def query_signedlist(wallet_id, args):
	obj = yixuan_yunchaoplus_agent_2(yunchaoplus.api_key,yunchaoplus.pk0_path, yunchaoplus.pkc_path, yunchaoplus.skc_path)
	example = obj.query_agent_objlist(wallet_id, args)
	return example


class yixuan_yunchaoplus_agent(yunchaoplusRequestObject):
	def __init__(self, api_key, pk0_path, pkc_path, skc_path):
		yunchaoplusRequestObject.__init__(self, api_key, pk0_path, pkc_path, skc_path)

	#创建签约对象  POST $endpoint/wallets/${wallet_id}/agents
	def create_agent_obj(self,request_data,wallet_id):
		url = 'https://%s/wallets/%s/agents'% (AGENTS_DNS,wallet_id)
		print('创建签约对象url:', url)
		return self.send(request_data, 'POST', url)
	

class yixuan_yunchaoplus_agent_2(yixuan_yunchaoplusRequestObject):
	def __init__(self, api_key, pk0_path, pkc_path, skc_path):
		yunchaoplusRequestObject.__init__(self, api_key, pk0_path, pkc_path, skc_path)

	#查询签约对象  GET $endpoint/wallets/${wallet_id}/agents/${id}
	def query_agent_obj(self,wallet_id, id):
		return self.send('GET', 'https://%s/wallets/%s/agents/%s' % (AGENTS_DNS,wallet_id,id))

	#查询签约对象列表   GET $endpoint/wallets/${wallet_id}/agents
	def query_agent_objlist(self, wallet_id, args):
		url = 'https://%s/wallets/%s/agents?count=%s&page=%s' % (AGENTS_DNS,wallet_id,args.get('count'),args.get('page'))
		if args.get('created_begin'):
			url = 'https://%s/wallets/%s/agents?count=%s&page=%s&created_begin=%s&created_end=%s' % (AGENTS_DNS,wallet_id,
			   args.get('count'),args.get('page'),args.get('created_begin'),args.get('created_end'))
		print('查询签约对象列表url:', url)
		return self.send('GET', url)	

	#删除签约对象  DELETE $endpoint/wallets/{wallet_id}/agents/${id}
	def delete_agent_obj(self,wallet_id,id):
		url = 'https://%s/wallets/%s/agents/%s' % (AGENTS_DNS,wallet_id,id)
		print('删除签约对象:', url, wallet_id,id)
		return self.send('DELETE','https://%s/wallets/%s/agents/%s' % (AGENTS_DNS,wallet_id,id))
