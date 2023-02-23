# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/5 18:22
# author：彭星荣
from conf import IO_yamls
import time
import yaml
import pytest
from logger import Logger


@pytest.fixture(scope='session', autouse=True)
def session():
    print('用例开始')
    yield
    IO_yamls.clean_yamls('script_files/coordinate.yaml')
    print('用例结束')


def edit_choice_yaml(configuration_text, button_choice, save_tip):
    logger = Logger.get_instance()
    data = configuration_text.toPlainText().split('\n')
    logger.info(data)
    path = '../script_files/' + button_choice.text() + '.yaml'
    with open(path, 'w', encoding='utf-8') as a:
        for n in range(len(data)):
            if data[n].find(',') != -1 and data[n].find('.') == -1 and data[n].find('鼠标') == -1:
                a.truncate()
                yaml.dump({'move' + str(n): [data[n]]}, a)
                button_choice.setText('配置保存成功')
                time.sleep(2)
                save_tip.setText('')
            elif data[n].find(',') == -1 and data[n].find('.') != -1 and data[n].find('鼠标') == -1:
                a.truncate()
                yaml.dump({'time' + str(n): data[n]}, a)
                button_choice.setText('配置保存成功')
                time.sleep(2)
                save_tip.setText('')
            elif data[n].find(',') == -1 and data[n].find('.') == -1 and data[n].find('鼠标') != -1:
                a.truncate()
                yaml.dump({'click' + str(n): str(data[n])}, a)
                button_choice.setText('配置保存成功')
                time.sleep(2)
                save_tip.setText('')
            else:
                print('文本框为空，理论上不会为空')

