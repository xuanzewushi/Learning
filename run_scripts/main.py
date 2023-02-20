# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2023/2/12
# author：SelDIs


import sys
from PyQt6.QtWidgets import *
from login_window import LoginDialog
from main_window import MainWindow
from register_window import RegisterDialog


# def main():
#     # 创建应用
#     window_application = QApplication(sys.argv)
#     # 设置登录窗口
#     login_ui = LoginDialog()
#     date = login_ui.exec()
#     # 校验是否验证通过
#     if date == 1:
#         print("进入主界面")
#         # 初始化主功能窗口
#         main_window = MainWindow()
#         # 展示窗口
#         main_window.show()
#         # 设置应用退出
#         sys.exit(window_application.exec())
#
#     elif date == 2:
#         print("进入注册界面")
#         # 初始化注册窗口
#         regis_window = RegisterDialog()
#         # 展示窗口
#         # regis_window.show()
#         # 设置应用退出
#         register_data = regis_window.exec()
#         # sys.exit(window_application.exec())
#         if register_data == 1:
#             login_ui.show()
#             sys.exit(window_application.exec())


def main():
    # 创建应用
    window_application = QApplication(sys.argv)
    # 设置登录窗口
    login_ui = LoginDialog()
    while True:
        date = login_ui.exec()
        # 校验进入哪个页面
        if date == 1:
            print("进入主界面")
            # 初始化主功能窗口
            main_window = MainWindow()
            # 展示窗口
            main_window.show()
            # 设置应用退出
            sys.exit(window_application.exec())

        elif date == 2:
            print("进入注册界面")
            # 初始化注册窗口
            regis_window = RegisterDialog()
            # 展示窗口
            regis_window.show()
            # 设置退出注册页面
            regis_window.exec()
            # sys.exit(window_application.exec())
            # if register_data == 1:
            #     login_ui.show()
            #     sys.exit(window_application.exec())


if __name__ == "__main__":
    main()


