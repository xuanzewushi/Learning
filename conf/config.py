#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: config.py
@time: 2023/2/22 下午4:26
"""
import sys
import platform
import os


is_py2 = sys.version_info < (3, 0)

if platform.system() == 'Linux':
    home_path = os.environ['HOME']
else:
    home_path = 'D://'


