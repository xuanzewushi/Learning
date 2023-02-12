# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/5 18:19
# author：彭星荣
"""
封装思路：
1.使用pytest模块
2.封装鼠标点击事件方法
3.封装yamls文件读取方法

编写思路：
1.调用yamls文件获取窗口title
2.根据title获取窗口句柄
3.根据句柄获取相对的无人机按钮位置
4.调用鼠标方法操作无人机，写一个按时间循环
"""
import time
import win32gui
from run_scripts import mouse_event
from conf import IO_yamls


class Execute:
    def execute(*path, ts=20):
        m = 0
        while m < ts:
            m += 1
            i = 0
            user_data = IO_yamls.read_yamls('script_files/coordinate.yaml')
            for n in user_data:
                # 唤醒窗口
                handle_x = n['x']
                handle_y = n['y']
                awaken = win32gui.WindowFromPoint((handle_x, handle_y))
                win32gui.SetForegroundWindow(awaken)

                # 获取操作步骤
                a = path[0]
                f_path = 'script_files/' + path[i] + '.yaml'
                step = IO_yamls.read_yamls(f_path)
                print(step)
                for k, v in step.items():
                    time.sleep(0.5)
                    if k[0:4] == 'move':
                        hd_x = int(v[0]) + handle_x
                        hd_y = int(v[1]) + handle_y
                        print(hd_x, hd_y)
                        mouse_event.mouse_event([hd_x, hd_y])
                    elif k[0:5] == 'click':
                        if v[2:4] == '左击':
                            print('左击')
                            mouse_event.mouse_event('left_event')
                        else:
                            print('右击')
                            mouse_event.mouse_event('right_event')
                    elif k[0:4] == 'time':
                        if i == 0 and v > 5:
                            time.sleep(3)
                            i = 0
                        elif i == 0 and v < 5:
                            time.sleep(v)
                        elif i == 1 and v > 5:
                            time.sleep(v)
                            i = 1
                        elif i == 1 and v < 5:
                            time.sleep(v)
                        else:
                            print('出现其他情况了')
                    else:
                        pass




