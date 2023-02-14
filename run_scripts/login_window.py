# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2023/2/12
# author：SelDIs

import sys
import time

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from register_window import RegisterDialog


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('登录界面')
        self.resize(400, 400)
        self.setFixedSize(self.width(), self.height())
        # self.setGeometry(500, 500, 500, 500)  # 窗口位置x，y，窗口尺寸x，y

        # 居中显示
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.status_tip = QLabel(' ')
        self.account_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.login_grid = QGridLayout()

        #
        self.login_win()

    def login_win(self):
        # 内容
        account_tip = QLabel('账号：')
        password_tip = QLabel('密码：')
        top_tip = QLabel(' ')
        # 输入框以及输入框内的提示文案
        self.account_edit.setPlaceholderText("请输入账号")
        self.password_edit.setPlaceholderText("请输入密码")

        # 设置按钮
        ok_button = QPushButton()
        ok_button.setText("登录")
        # 绑定按钮事件
        ok_button.clicked.connect(self.okbutton_clicked_status)

        register_button = QPushButton()
        register_button.setText("注册")
        # 绑定按钮事件
        register_button.clicked.connect(self.register_clicked_status)

        # 设置grid页面布局
        self.setLayout(self.login_grid)
        self.login_grid.setSpacing(6)

        # 设置内容布局
        self.login_grid.addWidget(top_tip, 1, 0, 1, 7)
        self.login_grid.addWidget(account_tip, 2, 1)
        self.login_grid.addWidget(self.account_edit, 2, 2, 1, 4)
        self.login_grid.addWidget(password_tip, 3, 1)
        self.login_grid.addWidget(self.password_edit, 3, 2, 1, 4)
        self.login_grid.addWidget(ok_button, 4, 3)
        self.login_grid.addWidget(register_button, 4, 4)
        self.login_grid.addWidget(self.status_tip, 5, 2, 1, 5)

    def okbutton_clicked_status(self):
        """
        调用数据库，将输入的数据与数据库数据对比
        """
        # 账号判断
        if self.account_edit.text() != "123":
            self.status_tip.setText("账号密码输入错误，请输入正确的账号密码")
            return

        # 密码判断
        if self.password_edit.text() != "1234":
            self.status_tip.setText("账号密码输入错误，请输入正确的账号密码")
            return

        # 通过验证，关闭对话框并返回1
        self.done(1)

    def register_clicked_status(self):
        # 关闭对话框并返回2
        self.done(2)

