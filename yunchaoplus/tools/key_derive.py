from ctypes import *
import os
import sys
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
# sys.path.append(BASE_DIR)

# # print('ssss', os.getcwd())
# # print(os.path.abspath(os.path.join(os.getcwd(), "../..")))
# path = os.path.abspath(os.path.join(os.getcwd(), ".."))

# sys.path.append(path)

# path = os.path.abspath(os.path.join(os.getcwd(), "..")) + "/yunchaoplus/tools/libderive_key.dll"
# os.chdir(path)

# import _win32sysloader 
# mod ='libderive_key'
# path_to_mod = _win32sysloader.LoadModule(mod)
# _derive_key = cdll.LoadLibrary(path_to_mod)

abs_path = os.path.abspath(__file__)

# print('本文件的绝对路径：', abs_path)

path2 = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


import platform
import struct

## python 位数
py_bit = struct.calcsize("P")

sys_bit = platform.architecture()[0]

def Is64():
    return sys_bit == '64bit'


if platform.system().lower() == 'windows':
    if Is64():
        if py_bit != 4:
            abs_path = path2 + '/util/libderive_key_64.dll'
        else:
            abs_path = path2 + '/util/libderive_key_32.dll'
    else:
        abs_path = path2 + '/util/libderive_key_32.dll'
elif platform.system().lower() == 'linux':
    if Is64():
        if py_bit != 4:
            abs_path = path2 + '/util/libderive_key_64.so'
        else:
            abs_path = path2 + '/util/libderive_key_32.so'
    else:
        abs_path = path2 + '/util/libderive_key_32.so'

_derive_key = cdll.LoadLibrary(abs_path)

class Py32LengthKey:
    def __init__(self, key):
        self.key = bytearray(key)

class SharedKey(Structure):
    _fields_ = [
        ("key", c_byte * 32),
    ]

class PublicKey(Structure):
    _fields_ = [
        ("key", c_byte * 32),
    ]

class SecretKey(Structure):
    _fields_ = [
        ("key", c_byte * 32),
    ]

class Random(Structure):
    _fields_ = [
        ("key", c_byte * 32),
    ]

    
class Signature(Structure):
    _fields_ = [
        ("key", c_byte * 64),
    ]

class Keypair(Structure):
    _fields_ = [
        ("secret_key", SecretKey),
        ("public_key", PublicKey),
        ("random_code", Random),
    ]

_derive_key.ristretto255_key_gen_from_seed.argtypes = [POINTER(c_char)]
_derive_key.ristretto255_key_gen_from_seed.restype = Keypair

def ristretto255_key_gen_from_seed(b):
    keypair = _derive_key.ristretto255_key_gen_from_seed(b)
    return keypair

_derive_key.ristretto255_dh.argtypes = [PublicKey, SecretKey]
_derive_key.ristretto255_dh.restype = SharedKey

def ristretto255_dh(pk, sk):
    p = _derive_key.ristretto255_dh(pk, sk)
    return Py32LengthKey(p.key)

_derive_key.ristretto255_derive_secret_key.argtypes = [SecretKey, Random, Random]
_derive_key.ristretto255_derive_secret_key.restype = Keypair

def ristretto255_derive_secret_key(sk, i, r):
    return _derive_key.ristretto255_derive_secret_key(sk, i, r)
    # return Py32LengthKey(p.key)
     
_derive_key.ristretto255_derive_public_key.argtypes = [PublicKey, Random, Random]
_derive_key.ristretto255_derive_public_key.restype = Keypair

def ristretto255_derive_public_key(pk, i, r):
    return _derive_key.ristretto255_derive_public_key(pk, i, r)

_derive_key.ristretto255_sign.argtypes = [SecretKey, PublicKey, POINTER(c_byte), c_size_t, Random]
_derive_key.ristretto255_sign.restype = Signature

def ristretto255_sign(sk, pk, m, r):
    length = len(m)
    ptr = cast(m, POINTER(c_byte))
    return _derive_key.ristretto255_sign(sk, pk, ptr, length, r)

_derive_key.ristretto255_verify.argtypes = [Signature, PublicKey, POINTER(c_byte), c_size_t]
_derive_key.ristretto255_verify.restype = c_bool

def ristretto255_verify(s, pk, m):
    length = len(m)
    ptr = cast(m, POINTER(c_byte))
    return _derive_key.ristretto255_verify(s, pk, ptr, length)

def _main():
    import secrets
    # import numpy as np
    seed1 = secrets.token_bytes(32)
    kp1 = ristretto255_key_gen_from_seed(seed1)

    # seed2 = secrets.token_bytes(32)
    # kp2 = ristretto255_key_gen_from_seed(seed2)
    # res1 = ristretto255_dh(kp1.public_key, kp2.secret_key)
    # res2 = ristretto255_dh(kp2.public_key, kp1.secret_key)

    # kp_sub1 = ristretto255_derive_secret_key(kp1.secret_key, kp1.random_code, kp1.random_code)
    # kp_sub2 = ristretto255_derive_public_key(kp1.public_key, kp1.random_code, kp1.random_code)

    # print(bytes(kp_sub1.public_key.key))
    # print(bytes(kp_sub2.public_key.key))
    # print(bytes(kp_sub1.public_key.key) == bytes(kp_sub2.public_key.key))

    # message = b'asdasda'
    # m = cast(message, POINTER(c_byte))
    # r = ristretto255_sign(kp1.secret_key, kp1.public_key, m, len(message), kp1.random_code)
    # print(bytes(r.key))


if __name__ == '__main__':
    # import secrets
    # seed1 = secrets.token_bytes(32)
    # kp1 = ristretto255_key_gen_from_seed(seed1)

    # sk = bytes(kp1.secret_key.key)
    # print(type(sk))

    # for _ in range(10):
    _main()
