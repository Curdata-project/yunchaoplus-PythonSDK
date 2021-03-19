# coding=utf-8

import nacl.utils
from nacl.public import PublicKey as PublicKeyNaCl
from nacl.public import PrivateKey as PrivateKeyNaCl
from nacl.public import Box as BoxNaCl
from nacl.encoding import Base64Encoder

# Pk 公钥 BASE64编码
# Sk 私钥 BASE64编码
# plaintext 明文数据 即原请求body做JSON化得到的字符串
# nonce 加密随机数 BASE64编码
# ciphertext 密文数据 BASE64编码

def Encrypt_NaCl(Pk, Sk, plaintext):
    Sk = PrivateKeyNaCl(Sk, encoder=Base64Encoder)
    Pk =  PublicKeyNaCl(Pk, encoder=Base64Encoder)
    box = BoxNaCl(Sk, Pk)
    # import numpy as np
    # print np.fromstring(box.shared_key(), dtype=np.uint8)
    nonce = nacl.utils.random(BoxNaCl.NONCE_SIZE)
    ciphertext = box.encrypt(plaintext, nonce, encoder=Base64Encoder)
    nonce = ciphertext.nonce
    ciphertext = ciphertext.ciphertext
    return ciphertext, nonce

def Decrypt_NaCl(Pk, Sk, nonce, ciphertext):
    Sk = PrivateKeyNaCl(Sk, encoder=Base64Encoder)
    Pk =  PublicKeyNaCl(Pk, encoder=Base64Encoder)
    nonce = Base64Encoder.decode(nonce)
    box = BoxNaCl(Sk, Pk)
    # import numpy as np
    # print np.fromstring(box.shared_key(), dtype=np.uint8)
    plaintext = box.decrypt(ciphertext, nonce, encoder=Base64Encoder)
    return plaintext