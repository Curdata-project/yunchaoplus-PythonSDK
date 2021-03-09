# coding=utf-8

from .crypto import *
import json
import base64

import requests
import sys
from os import urandom
from base64 import b64encode

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


class yunchaoplusRequestObject():

    def __init__(self, api_key, pk0_path, pkc_path, skc_path):
        self.api_key = api_key
        # self.request_url = request_url
        self.pk0_path = pk0_path # 平台公钥路径
        self.pkc_path = pkc_path # 商家公钥路径
        self.skc_path = skc_path # 商家私钥路径
        # request_data = json.dumps(request_data)
        # self.request_method = request_method

    def send(self, request_data, request_method, request_url):
        request_data = json.dumps(request_data)
        # Request Part
        # --------------------------

        Pk1, Sk1, R = genPK1()

        try:
            with open(self.pk0_path, 'r') as f:
                self.Pk0 = f.read()
        except IOError as err:
            # print("File Error:"+str(err)) #str()将对象转换为字符串
            print('平台公钥路径错误')
            return 

        try:
            with open(self.pkc_path, 'r') as f:
                self.Pkc = f.read()
        except IOError as err:
            print('商家公钥路径错误')
            return 

        try:
            with open(self.skc_path, 'r') as f:
                self.Skc = f.read()
        except IOError as err:
            print('商家私钥路径错误')
            return 
        # with open(self.pk0_path, 'r') as f:
        #     self.Pk0 = f.read()
        # with open(self.pkc_path, 'r') as f:
        #     self.Pkc = f.read()
        # with open(self.skc_path, 'r') as f:
        #     self.Skc = f.read()

        S = CreateSharedKey(self.Pk0, Sk1)  # 平台公钥Pk0和临时私钥Sk1计算对称密钥S

        ciphertext = SharedEncrypt(request_data, S)

        if PY3:
            payload = {
                "version": 1,
                "payload": ciphertext.decode(),
                "Pk1": Pk1.decode(),
                "sign": Sign(self.Skc, self.Pkc, ciphertext+Pk1, R).decode()
            }
        else:
            payload = {
                "version": 1,
                "payload": ciphertext,
                "Pk1": Pk1,
                "sign": Sign(self.Skc, self.Pkc, ciphertext+Pk1, R)
            }

        payload = json.dumps(payload, ensure_ascii=False)
        print('负载内容：', type(payload), payload)
        r = getattr(requests, request_method.lower())(request_url, headers={
            "X-API-KEY": self.api_key, "Content-Type": "application/json"}, data=payload)

        # Response Part
        # --------------------------
        print('请求结果:', r.status_code, r.text)
        if r.status_code != 200:
            return '请求失败'
        data = r.json()

        if PY3:
            Pk1 = data["Pk1"].encode('utf-8')
            payload = data["payload"].encode('utf-8')
            sign = data["sign"].encode('utf-8')
            result = Verify(sign, self.Pk0.encode('utf-8'), payload+Pk1)
            print('校验结果：', data, Verify(
                    sign, self.Pk0.encode('utf-8'), payload+Pk1))
        else:
            Pk1 = data["Pk1"]
            payload = data["payload"]
            sign = data["sign"]
            result = Verify(sign, self.Pk0, str(payload+Pk1))
        if result:

            S = CreateSharedKey(Pk1, self.Skc)  # 临时公钥Pk1和用户私钥Skc计算对称密钥S

            plaintext = SharedDecrypt(payload, S)

            return json.loads(plaintext)

        else:
            return

class yixuan_yunchaoplusRequestObject(yunchaoplusRequestObject):
	def __init__(self, api_key, pk0_path, pkc_path, skc_path):
		yunchaoplusRequestObject.__init__(self, api_key, pk0_path, pkc_path, skc_path)

	def send(self, request_method, request_url):
		bytes_16 = urandom(16)
		bytes_16 = b64encode(bytes_16).decode('utf-8')
		request_data = {'random':bytes_16}
		return super().send(request_data, request_method, request_url)
