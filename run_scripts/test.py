# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/7 15:55
# author：彭星荣
import yaml
from run_scripts import main_window
import sqlite3

# with open('script_files/配置二.yaml', 'r', encoding='utf-8') as r:
#     data = yaml.load(r, Loader=yaml.FullLoader)
#     print(data)
# a = [1, 2]
# b = '1.2,3'
# print(b.find('8'))
# conn = sqlite3.connect('./script_files/register_sqlite.db')
# cursor = conn.cursor()
# # cursor.execute('select * from user where id=?', ('1',))
# # conn = sqlite3.connect('test.db')
# # cursor = conn.cursor()
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20), password varchar(20))')
# # cursor.execute('create table user (id varchar(20) primary key, name varchar(20)), password varchar(20)')
# cursor.execute('insert into user (id, name, password) values (\'1\', \'admin\', \'admin\')')
# conn.commit()
#
# # print(cursor.fetchall())
# cursor.close()
# conn.close()

from run_scripts.register_sqlite import execute_register_data

reg = execute_register_data("select * from user")
print(reg)
# conn = sqlite3.connect('./script_files/register_sqlite.db')
# cursor = conn.cursor()
# # cursor.execute('create table user (id varchar(20) primary key, name varchar(20), password varchar(20))')
# # cursor.execute('insert into user (id, name, password) values (\'1\', \'admin\', \'admin\')')
# # conn.commit()
# cursor.execute("select * from user")
# print(cursor.fetchall())
# cursor.close()
# conn.close()

