# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/5 18:15
# author：彭星荣

import win32api
import win32con


def mouse_event(event):
    if event == 'left_event':
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        return '鼠标左击'
    elif event == 'right_event':
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
        return '鼠标右击'
    elif type(event) is list:
        win32api.SetCursorPos((event[0], event[1]))
        return '鼠标移动到{}{}'.format(event[0], event[1])
    else:
        return '没有任何操作'

