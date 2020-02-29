# encoding=utf8
# conn_db
# by hyn
# 20200229

import conn_db

sql='show tables'
insert="insert into tender_info (name,company,view_cont,release_time) values ('招标公告名称测试5','招标公司测试','123','20200229')"
select='select * from tender_info'

#result=conn_db.conn(sql)
#result=conn_db.conn(insert)
result=conn_db.conn(select)

print(result)
