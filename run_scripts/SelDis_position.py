# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/6 10:07
# author：彭星荣
from conf import IO_yamls
import win32gui


class Position(object):
    def get_position(self):
        win_title = IO_yamls.read_yamls('script_files/win_title.yaml')
        n = 0
        for k, v in win_title.items():
            if k[0:9] == 'win_title':
                n += 1
                wt = win_title['win_title' + str(n)]
                handle = win32gui.FindWindow(None, wt)
                if handle != 0:
                    pt = win32gui.GetWindowRect(handle)
                    IO_yamls.write_yamls([{'x': pt[0], 'y': pt[1]}], 'script_files/coordinate.yaml')
                    return '1'
                else:
                    return '0'


if __name__ == '__main__':
    Position()
    print(type(Position().get_position()))
