# encoding=utf8
# conn_db
# by hyn
# 20200229

import pymysql


def conn(sql):
    # 连接database
    conn = pymysql.connect(host='127.0.0.1', user='root', password='test', database='tender', charset='utf8')
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()

    # 执行SQL语句
    cursor.execute(sql)

    result = cursor.fetchall()

    # 关闭光标对象
    cursor.close()

    conn.commit()
    # 关闭数据库连接
    conn.close()

    return result
