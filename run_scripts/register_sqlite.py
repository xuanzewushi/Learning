#!/usr/bin/env python
# encoding: utf-8

import sqlite3


# 调用数据库
def execute_register_data(execute):
    conn = sqlite3.connect('../script_files/register_sqlite.db')
    cursor = conn.cursor()
    if execute.split(' ')[0] == "insert":
        # 输入
        # data = 'insert into user ({}) values({})'.format(table_columns, table_values)
        cursor.execute(execute)
        # 提交
        conn.commit()
        print("提交成功！")
    elif execute.split(' ')[0] == "select":
        # 查询
        cursor.execute(execute)
        return cursor.fetchall()

    else:
        pass

    print('关闭数据库')
    cursor.close()
    conn.close()







