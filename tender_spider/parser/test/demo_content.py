# encoding=utf8
# demo test for tender spider
# by hyn
# 20200308


import urllib.request
import simplejson

import requests
import tender_spider.parser.test.sample_parser as sample_parser
import tender_spider.parser.test.content_parser as content_parser

# url = 'http://www.hngp.gov.cn/henan/list2?channelCode=0101&pageSize=16&bz=1&gglx=0&pageNo=1'
# url = 'http://www.hngp.gov.cn/webfile/henan/cgxx/cggg/webinfo/2020/02/03/426901.htm'
url = 'http://www.hngp.gov.cn/henan/content?infoId=423717&channelCode=H600101'
# response = requests.request("GET", url, headers=headers)
for i in range(1):
    response = requests.request("GET", url)

    # result = response.content.decode('utf-8')

    # print(result)
    # response=requests.get(url)
    # print(response.text)
    print('##################', i)
    content_parser.parser(response.content.decode('utf-8'))
