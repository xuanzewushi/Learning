# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2023/2/12
# author：SelDIs


import sys
from PyQt6.QtWidgets import *
from login_window import LoginDialog
from main_window import MainWindow


def main():
    # 创建应用
    window_application = QApplication(sys.argv)
    # 设置登录窗口
    login_ui = LoginDialog()
    # 校验是否验证通过
    if login_ui.exec() == 1:
        # 初始化主功能窗口
        main_window = MainWindow()
        # 展示窗口
        main_window.show()
        # 设置应用退出
        sys.exit(window_application.exec())


if __name__ == "__main__":
    main()


