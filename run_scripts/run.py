# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/6 10:07
# author：彭星荣
import pytest
from position import Position
from run_scripts.Execution_profile import Execute


class TestEdit:

    def test_run(self):
        # 调用获取窗口
        pos_data = Position().get_position()
        print(type(pos_data))
        # 判断窗口数据文件是否为空
        if int(pos_data) == 0:
            print('没有获取到任何窗口初始坐标。')
        else:
            # 调用执行配置文件
            # Execute.execute('配置一')
            # Execute.execute('配置一', '配置二')
            pass


if __name__ == '__main__':
    pytest.main(['-s'])

