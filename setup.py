# -*- coding: utf-8 -*-
# author: 逸轩
# desc: yunchaoplus 安装
# date: 2021-02-22

import os
import sys
import warnings
from version import VERSION


path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = []

if sys.version_info < (2, 6):
    warnings.warn(
        DeprecationWarning)
    install_requires.append('requests >= 0.8.8, < 0.10.1')
    install_requires.append('ssl')
else:
    install_requires.append('requests >= 0.8.8')
    # install_requires.append('pyOpenSSL==20.0.1')

install_requires.append('PyNaCl==1.4.0')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

if PY2:
	with open('LONG_DESCRIPTION.rst') as f:
		long_description = f.read()
else:
	with open('LONG_DESCRIPTION.rst', encoding='utf-8') as f:
		long_description = f.read()

# Don't import yunchaoplus module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'yunchaoplus'))

# Get simplejson if we don't already have json
if sys.version_info < (3, 0):
    try:
        from util import json  
    except ImportError:
        install_requires.append('simplejson')


setup(
    name='yunchaoplus',
    packages=['yunchaoplus', 'yunchaoplus.api_resources','yunchaoplus.tools'
              ],
    version=VERSION,
    description='python SDK bindings by yixuan',
    long_description=long_description,
    author='yixuan',
    author_email='',
    url='https://github.com/Curdata-project/yunchaoplus_auth/tree/SDK-Python',
    package_data={'yunchaoplus': []},
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
