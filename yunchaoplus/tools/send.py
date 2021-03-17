# coding=utf-8

from .crypto import *
import json
import base64
import requests
import os

class yunchaoplusRequestObject(object):

    def __init__(self, api_key, pk0_path, pkc_path, skc_path):
        self.api_key = api_key
        # self.request_url = request_url
        self.pk0_path = pk0_path
        self.skc_path = skc_path
        # self.request_data = json.dumps(request_data)
        # self.request_method = request_method

    def send(self, request_data, request_method, request_url):
        
        # Request Part
        # --------------------------
        
        try:
            with open(self.pk0_path, 'r') as f:
                self.Pk0 = f.read()
        except IOError as err:
            # print("File Error:"+str(err)) #str()将对象转换为字符串
            print('平台公钥路径错误')
            return 

        # try:
        #     with open(self.pkc_path, 'r') as f:
        #         self.Pkc = f.read()
        # except IOError as err:
        #     print('商家公钥路径错误')
        #     return 

        try:
            with open(self.skc_path, 'r') as f:
                self.Skc = f.read()
        except IOError as err:
            print('商家私钥路径错误')
            return 
        
        ciphertext, nonce = Encrypt_NaCl(self.Pk0, self.Skc, json.dumps(request_data))

        payload = {
            "version": 2,
            "payload": ciphertext,
            "nonce": nonce
        }

        r = getattr(requests, request_method.lower())(request_url, headers={"X-API-KEY": self.api_key}, json=payload)

        # Response Part
        # --------------------------
        
        data = r.json()

        payload = data["payload"]
        nonce = data["nonce"]

        plaintext = Decrypt_NaCl(self.Pk0, self.Skc, nonce, payload)

        return plaintext

class GET_yunchaoplusRequestObject(yunchaoplusRequestObject):
	def send(self, request_method, request_url):
		bytes_16 = os.urandom(16)
		bytes_16 = base64.b64encode(bytes_16).decode('utf-8')
		request_data = {'random':bytes_16}
		return super(GET_yunchaoplusRequestObject, self).send(request_data, request_method, request_url)