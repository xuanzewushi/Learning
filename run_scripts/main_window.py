# !/usr/bin/python
# -*- coding:utf-8 -*-
# 2022/10/6 22:45
# author：SelDIs

import sys
import time

import yaml
from PyQt6.QtWidgets import *
from conf import IO_yamls


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_win()
        self.setGeometry(500, 500, 500, 500)  # 窗口位置x，y，窗口尺寸x，y
        # 居中显示
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # 窗口title
        self.setWindowTitle('配置界面')
        self.show()

    def main_win(self):
        # test push git
        # 说明文案区
        configuration_one = QLabel('一、编辑配置前先点击配置一/配置二/配置三\n'
                                   '二、在右边输入配置后点击对应的写入按钮，将配置写入到配置文档区')
        # 左边配置按钮
        self.buntton_one = QPushButton('配置一')
        self.buntton_one.clicked.connect(self.configuration_one)
        self.buntton_two = QPushButton('配置二')
        self.buntton_two.clicked.connect(self.configuration_two)
        self.buntton_three = QPushButton('配置三')
        self.buntton_three.clicked.connect(self.configuration_three)
        self.buntton_choice = QLabel('请先选择配置文件')

        # 配置文本框
        self.configuration_text = QTextEdit()
        self.configuration_text.setPlaceholderText('请选择配置')
        self.configuration_text.setReadOnly(True)
        # 右边编辑配置区
        self.coordinate_label = QLabel('坐标:')
        self.coordinate_x = QLineEdit()
        self.coordinate_x.setPlaceholderText('x坐标')
        self.coordinate_y = QLineEdit()
        self.coordinate_y.setPlaceholderText('y坐标')
        self.coordinate_x.resize(1, 2)
        self.coordinate_y.resize(2, 3)
        self.coordinate_button = QPushButton('写入坐标')
        self.coordinate_button.clicked.connect(self.edit_coordinate)
        self.mouse_left_click = QPushButton('鼠标左击')
        self.mouse_left_click.clicked.connect(self.left_click)
        self.mouse_right_click = QPushButton('鼠标右击')
        self.mouse_right_click.clicked.connect(self.right_click)
        self.sleep_time = QLabel('时间:')
        self.sleep_time_edit = QLineEdit()
        self.sleep_time_edit.setPlaceholderText('单位:s')
        self.sleep_time_button = QPushButton('写入时间')
        self.sleep_time_button.clicked.connect(self.t_edit)
        self.clear_text = QPushButton('删除上一个配置')
        self.clear_text.clicked.connect(self.text_clear)
        self.clear_text_all = QPushButton('删除全部配置')
        self.clear_text_all.clicked.connect(self.text_clear_all)
        self.save_text = QPushButton('保存配置')
        self.save_text.clicked.connect(self.save_configuration)
        self.seve_tip = QLabel()

        # self.test = QPushButton('执行')
        # self.test.clicked.connect(self.showDialog)

        grid = QGridLayout()
        grid.setSpacing(5)
        # 说明文案区
        grid.addWidget(configuration_one, 1, 0, 1, 6)  # x, y, n, m。x是第几行，y是第几列，n是占多少行，m是多少列
        # grid.addWidget(self.test, 1, 7)

        # 左边配置按钮
        grid.addWidget(self.buntton_one, 2, 0)
        grid.addWidget(self.buntton_two, 2, 1)
        grid.addWidget(self.buntton_three, 2, 2)
        grid.addWidget(self.buntton_choice, 2, 4, 1, 2)

        # 配置文本框
        grid.addWidget(self.configuration_text, 3, 0, 6, 3)

        # 右边编辑配置区
        grid.addWidget(self.coordinate_label, 3, 3)
        grid.addWidget(self.coordinate_x, 3, 4)
        grid.addWidget(self.coordinate_y, 3, 5)
        grid.addWidget(self.coordinate_button, 3, 6)
        grid.addWidget(self.mouse_left_click, 5, 4)
        grid.addWidget(self.mouse_right_click, 5, 5)
        grid.addWidget(self.sleep_time, 4, 3)
        grid.addWidget(self.sleep_time_edit, 4, 4, 1, 2)
        grid.addWidget(self.sleep_time_button, 4, 6)
        grid.addWidget(self.clear_text, 6, 4)
        grid.addWidget(self.clear_text_all, 6, 5)
        grid.addWidget(self.save_text, 8, 4, 1, 2)
        grid.addWidget(self.seve_tip, 7, 4, 1, 2)

        self.setLayout(grid)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭', "是否关闭程序?")
        if str(reply) == 'StandardButton.Yes':
            event.accept()
        else:
            event.ignore()

    def w_yaml(self):
        if self.buntton_choice.text() != '请先选择配置文件':
            if self.configuration_text.toPlainText() != '':
                dt = self.configuration_text.toPlainText()
                data = dt.split('\n')
                path = '../script_files/' + self.buntton_choice.text() + '.yaml'
                with open(path, 'w', encoding='utf-8') as a:
                    for n in range(len(data)):
                        if data[n].find(',') != -1 and data[n].find('.') == -1 and data[n].find('鼠标') == -1:
                            a.truncate()
                            yaml.dump({'move' + str(n): [data[n]]}, a)
                            self.buntton_choice.setText('配置保存成功')
                            time.sleep(2)
                            self.seve_tip.setText('')
                        elif data[n].find(',') == -1 and data[n].find('.') != -1 and data[n].find('鼠标') == -1:
                            a.truncate()
                            yaml.dump({'time' + str(n): data[n]}, a)
                            self.buntton_choice.setText('配置保存成功')
                            time.sleep(2)
                            self.seve_tip.setText('')
                        elif data[n].find(',') == -1 and data[n].find('.') == -1 and data[n].find('鼠标') != -1:
                            a.truncate()
                            yaml.dump({'click' + str(n): str(data[n])}, a)
                            self.buntton_choice.setText('配置保存成功')
                            time.sleep(2)
                            self.seve_tip.setText('')
                        else:
                            print('文本框为空，理论上不会为空')
            else:
                self.information('写入配置')
        else:
            self.information('选择配置文件')

    def massage(self, tid, dt1=None, dt2=None):
        p_text = self.buntton_choice.text()
        if p_text != '请先选择配置文件':
            if tid == 1:
                self.configuration_text.append(dt1)
            elif tid == 2:
                if dt1 != '' and dt2 != '':
                    self.configuration_text.append(dt1 + ',' + dt2)
                else:
                    self.information('填写坐标')
            elif tid == 3:
                if str(dt1) != '':
                    self.configuration_text.append(dt1)
                else:
                    self.information('填写时间')
            else:
                print('无法识别的id')
        else:
            self.information('选择配置文件')

    def information(self, mass):
        information = QMessageBox.information(self, '警告！', '请先' + mass)

    # 调用读取文件方法区
    def configuration_one(self):
        self.buntton_choice.setText('配置一')
        self.configuration_text.setText('\n'.join(IO_yamls.r_yaml('配置一')))

    def configuration_two(self):
        self.buntton_choice.setText('配置二')
        self.configuration_text.setText('\n'.join(IO_yamls.r_yaml('配置二')))

    def configuration_three(self):
        self.buntton_choice.setText('配置三')
        self.configuration_text.setText('\n'.join(IO_yamls.r_yaml('配置三')))

    # 调用信息弹窗区
    def edit_coordinate(self):
        self.massage(2, self.coordinate_x.text(), self.coordinate_y.text())

    def left_click(self):
        self.massage(1, self.mouse_left_click.text())

    def right_click(self):
        self.massage(1, self.mouse_right_click.text())

    def t_edit(self):
        self.massage(3, self.sleep_time_edit.text())

    def text_clear(self):
        if self.buntton_choice.text() != '请先选择配置文件':
            text = self.configuration_text.toPlainText()
            data = text.split('\n')
            data.pop(-1)
            self.configuration_text.setText('\n'.join(data))
        else:
            self.information('选择配置文件')

    def text_clear_all(self):
        if self.buntton_choice.text() != '请先选择配置文件':
            self.configuration_text.clear()
        else:
            self.information('选择配置文件')

    def save_configuration(self):
        self.w_yaml()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     plugin = MainWindow()
#     sys.exit(app.exec())







