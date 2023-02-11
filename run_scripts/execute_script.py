# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/19 19:03
# author：彭星荣

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from conf import IO_yamls
from run_scripts.SelDis_Execution_profile import Execute


class ExecuteScript(QWidget):
    def __init__(self):
        super().__init__()
        self.execute()

    def execute(self):
        # 控件属性
        self.configuration = QTextEdit()
        self.configuration.setPlaceholderText('请选择配置')
        self.configuration.setReadOnly(True)
        self.configuration_one = QPushButton('配置一')
        self.configuration_one.clicked.connect(self.conf_one)
        self.configuration_two = QPushButton('配置二')
        self.configuration_two.clicked.connect(self.conf_two)
        self.configuration_three = QPushButton('配置三')
        self.configuration_three.clicked.connect(self.conf_three)
        self.execute_button = QPushButton('执行')
        self.execute_button.clicked.connect(self.execute_mass)
        self.execute_time_tip = QLabel('执行次数：')
        self.execute_time = QLineEdit()
        self.execute_time.setPlaceholderText('请输入循环执行次数')
        self.choice_tip = QLabel('请先选择要执行的配置文件')

        # 布局
        grid = QGridLayout()
        grid.addWidget(self.configuration, 2, 1, 3, 1)
        grid.addWidget(self.configuration_one, 2, 2, 1, 1)
        grid.addWidget(self.configuration_two, 2, 2, 2, 1)
        grid.addWidget(self.configuration_three, 2, 2, 3, 1)
        grid.addWidget(self.execute_button, 7, 1, 2, 3)
        grid.addWidget(self.execute_time_tip, 5, 1)
        grid.addWidget(self.execute_time, 6, 1, 1, 2)
        grid.addWidget(self.choice_tip, 1, 1)

        self.setLayout(grid)
        # 窗口属性
        self.setGeometry(600, 300, 400, 300)
        self.setWindowTitle('执行配置')
        self.show()

    def conf_one(self):
        self.choice_tip.setText('已选择配置一')
        self.configuration.setText('\n'.join(IO_yamls.r_yaml('配置一')))

    def conf_two(self):
        self.choice_tip.setText('已选择配置二')
        self.configuration.setText('\n'.join(IO_yamls.r_yaml('配置二')))

    def conf_three(self):
        self.choice_tip.setText('已选择配置三')
        self.configuration.setText('\n'.join(IO_yamls.r_yaml('配置三')))

    def execute_mass(self):
        reply = QMessageBox.question(self, '正在执行配置', '正在执行' + self.choice_tip.text()[-1:-3])
        if self.choice_tip.text() != '请先选择要执行的配置文件':
            Execute.execute(self.choice_tip.text()[-1:-3], int(self.execute_time.text()))
            if str(reply) == 'StandardButton.Yes':
                self.close()
            else:
                pass

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭', "是否关闭程序?")
        if str(reply) == 'StandardButton.Yes':
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = ExecuteScript()
    sys.exit(app.exec())
