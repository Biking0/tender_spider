# encoding=utf8
# demo test for tender spider
# by hyn
# 20200106


import urllib.request
import simplejson

import requests
import tender_spider.parser.test.sample_parser as sample_parser

url = 'http://www.hngp.gov.cn/henan/list2?channelCode=0101&pageSize=16&bz=1&gglx=0&pageNo=1'
# response = requests.request("GET", url, headers=headers)
for i in range(1):
    response = requests.request("GET", url)

    # response=requests.get(url)
    #print(response.text)
    print('##################', i)
    sample_parser.parser(response.text)
