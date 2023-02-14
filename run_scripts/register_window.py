# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2023/2/12
# author：SelDIs

from PyQt6.QtWidgets import *
from register_sqlite import execute_register_data


class RegisterDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('注册界面')
        self.resize(400, 400)
        self.setFixedSize(self.width(), self.height())
        # self.setGeometry(500, 500, 500, 500)  # 窗口位置x，y，窗口尺寸x，y

        # 居中显示
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # 输入框
        self.account_edit = QLineEdit(self)
        self.password_edit = QLineEdit(self)
        self.label_tip = QLabel(' ', self)

        self.register_win()

    def register_win(self):
        # 内容
        QLabel('账号*：', self).move(100, 100)
        QLabel('密码*：', self).move(100, 140)
        self.label_tip.move(150, 300)
        top_tip = QLabel('1.带有*号的输入框是必填项。\n'
                         '2.账号/密码不得少于6位。', self)
        top_tip.move(100, 30)
        # 输入框以及输入框内的提示文案
        self.account_edit.move(150, 100)
        self.account_edit.setPlaceholderText("请输入账号")
        self.password_edit.move(150, 140)
        self.password_edit.setPlaceholderText("请输入密码")

        # 注册按钮
        register_button = QPushButton(self)
        register_button.setText("注册")
        register_button.move(150, 260)
        # 绑定按钮事件
        register_button.clicked.connect(self.register_clicked)

    def register_clicked(self):
        """
        调用数据库， 将数据传入数据库记录
        """
        account = self.account_edit.text()
        password = self.password_edit.text()
        # 先查询获取账号已记录的数量，然后数量+1写入id
        sel_data = len(execute_register_data('select * from user'))
        print(sel_data)
        data = 'insert into user (id, name, password) values({}, {}, {})'.format(sel_data+1, account, password)
        execute_register_data(data)
        self.label_tip.setText("注册成功")



