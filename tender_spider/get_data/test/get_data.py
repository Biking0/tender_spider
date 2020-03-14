# encoding=utf8
# 请求网站，获取数据
# by hyn
# 20200314

import requests

#url = 'http://www.hngp.gov.cn/henan/list2?channelCode=0101&pageSize=16&bz=1&gglx=0&pageNo=1'


# 通用网络请求方法
def get_data(url):
    response = requests.request("GET", url)

    return response.content
