# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/7 15:55
# author：彭星荣
import yaml
from run_scripts import PlugIn

with open('script_files/配置二.yaml', 'r', encoding='utf-8') as r:
    data = yaml.load(r, Loader=yaml.FullLoader)
    print(data)
# a = [1, 2]
# b = '1.2,3'
# print(b.find('8'))
