# encoding=utf8
# conn_db
# by hyn
# 20200229

import tender_spider.conn_db.test.conn_db as conn_db


# 入库简略信息
def save_sample_data(data):
    for data in data:
        sql = 'show tables'
        insert = "insert into tender_info (name,company,view_cont,release_time,url) values ('%s','%s','%s','%s','%s')" % (
            data[0], data[1], data[2], data[3], data[4])
        select = 'select * from tender_info'
        print(insert)
        # result=conn_db.conn(sql)
        try:
            result = conn_db.conn(insert)
        except Exception as e:
            print(e)
            continue
        # result=conn_db.conn(select)


# 入库详细信息
def save_content_data(data):
    # for data in data:
    sql = 'show tables'
    insert = "insert into tender_content (name,content) values ('%s','%s')" % (
        data[0], data[1])
    select = 'select * from tender_info'
    print(insert)
    # result=conn_db.conn(sql)
    try:
        result = conn_db.conn(insert)
    except Exception as e:
        print(e)
        # continue
    # result=conn_db.conn(select)
