# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2023/2/12
# author：SelDIs

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('登录界面')
        self.resize(200, 200)
        self.setFixedSize(self.width(), self.height())

        ###### 设置界面控件
        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.lineEdit_account = QLineEdit()
        self.lineEdit_account.setPlaceholderText("请输入账号")
        self.verticalLayout.addWidget(self.lineEdit_account)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText("请输入密码")
        self.verticalLayout.addWidget(self.lineEdit_password)

        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("确定")
        self.verticalLayout.addWidget(self.pushButton_enter)

        self.pushButton_quit = QPushButton()
        self.pushButton_quit.setText("取消")
        self.verticalLayout.addWidget(self.pushButton_quit)

        ###### 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.clicked_status)

    def clicked_status(self):
        # 账号判断
        if self.lineEdit_account.text() != "123":
            return

        # 密码判断
        if self.lineEdit_password.text() != "1234":
            return

        # 通过验证，关闭对话框并返回1
        self.accept()
