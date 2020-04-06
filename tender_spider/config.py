# encoding=utf8
# 通用配置文件
# by hyn
# 20200308

import os 
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

# 通用地址url
common_url = 'http://www.hngp.gov.cn/'

# 省级url
pro_url = 'http://www.hngp.gov.cn/henan/list2?pageNo=1&pageSize=16&bz=1&gglx=0'

# 省级翻页url
pro_page_url = 'http://www.hngp.gov.cn/henan/list2?channelCode=&bz=1&pageSize=16&gglx=0&pageNo='

# 市区县url
city_url = 'http://www.hngp.gov.cn/henan/list2?pageNo=1&pageSize=16&bz=2&gglx=0'

# 市区县翻页url
city_page_url = 'http://www.hngp.gov.cn/henan/list2?channelCode=&bz=2&pageSize=16&gglx=0&pageNo='
