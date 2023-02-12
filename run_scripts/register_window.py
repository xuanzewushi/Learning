# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2023/2/12
# author：SelDIs

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class RegisterDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('注册界面')
        self.resize(300, 300)
        self.setFixedSize(self.width(), self.height())
        # self.setGeometry(500, 500, 500, 500)  # 窗口位置x，y，窗口尺寸x，y

        # 居中显示
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())







