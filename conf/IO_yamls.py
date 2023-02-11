# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/5 18:14
# author：彭星荣
import yaml
import os


# 读取yaml文件
def read_yamls(file_name):
    f_path = os.path.join(os.path.abspath('../'), file_name)
    with open(f_path, 'r', encoding='utf-8') as r:
        return yaml.load(r, Loader=yaml.FullLoader)


# 写入yaml文件
def write_yamls(data, file_name):
    f_path = os.path.join(os.path.abspath('../'), file_name)
    with open(f_path, 'a', encoding='utf-8') as a:
        yaml.dump(data, a)
        return '写入成功'


# 清空yaml文件
def clean_yamls(file_name):
    f_path = os.path.join(os.path.abspath('../'), file_name)
    with open(f_path, 'w', encoding='utf-8') as c:
        c.truncate()
        return '清除成功'


#
def r_yaml(name):
    path = '../script_files/' + name + '.yaml'
    with open(path, 'r', encoding='utf-8') as r:
        data = yaml.load(r, Loader=yaml.FullLoader)
        text = []
        if data is not None:
            for v in data.values():
                text.append(str(v))
            return text
        else:
            return ''
# if __name__ == '__main__':
#     data = read_yamls('script_files/win_title.yaml')
#     print(data)


