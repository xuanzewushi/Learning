# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/5 18:22
# author：彭星荣
from conf import IO_yamls

import pytest


@pytest.fixture(scope='session', autouse=True)
def session():
    # IO_yamls.clean_yamls('script_files/coordinate.yaml')
    print('用例开始')
    yield
    # IO_yamls.clean_yamls('script_files/coordinate.yaml')
    print('用例结束')


