# coding=utf-8

from .key_derive import *

import nacl.secret
import secrets
import base64

import os
import ctypes

import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


def toC_type_32(p):
    return (ctypes.c_byte * 32).from_buffer_copy(p)


def toC_type_64(p):
    return (ctypes.c_byte * 64).from_buffer_copy(p)


def genPK1():
    seed1 = secrets.token_bytes(32)
    kp1 = ristretto255_key_gen_from_seed(seed1)

    return base64.b64encode(kp1.public_key.key), base64.b64encode(kp1.secret_key.key), base64.b64encode(kp1.random_code.key)


def SharedEncrypt(plaintext, SharedKey):
    print('明文类型:', type(plaintext))
    if PY3:
        plaintext = base64.b64encode(plaintext.encode('utf-8'))
    else:
        plaintext = base64.b64encode(plaintext)
    box = nacl.secret.SecretBox(bytes(SharedKey))
    ciphertext = box.encrypt(plaintext)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext


def SharedDecrypt(ciphertext, SharedKey):
    ciphertext = base64.b64decode(ciphertext)
    box = nacl.secret.SecretBox(bytes(SharedKey))
    plaintext = box.decrypt(ciphertext)
    plaintext = base64.b64decode(plaintext)
    return plaintext


def CreateSharedKey(Pk, Sk):
    Pk = base64.b64decode(Pk)
    Sk = base64.b64decode(Sk)

    StructurePk = PublicKey()
    StructurePk.key = toC_type_32(Pk)
    StructureSk = SecretKey()
    StructureSk.key = toC_type_32(Sk)

    res = ristretto255_dh(StructurePk, StructureSk)
    return res.key  # 必须32Byte!


def Sign(Sk, Pk, message, r):
    Pk = base64.b64decode(Pk)
    Sk = base64.b64decode(Sk)
    r = base64.b64decode(r)

    StructurePk = PublicKey()
    StructurePk.key = toC_type_32(Pk)
    StructureSk = SecretKey()
    StructureSk.key = toC_type_32(Sk)
    StructureR = Random()
    StructureR.key = toC_type_32(r)

    sign = ristretto255_sign(StructureSk, StructurePk, message, StructureR)
    sign = base64.b64encode(sign.key)
    return sign


def Verify(sign, Pk, message):
    sign = base64.b64decode(sign)
    Pk = base64.b64decode(Pk)

    StructureSign = Signature()
    StructureSign.key = toC_type_64(sign)
    StructurePk = PublicKey()
    StructurePk.key = toC_type_32(Pk)

    return ristretto255_verify(StructureSign, StructurePk, message)
