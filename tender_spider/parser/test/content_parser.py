# encoding=utf8
# 解析公告详细信息
# by hyn
# 20200308


import urllib.request
import simplejson
from bs4 import BeautifulSoup
import requests

import tender_spider.config as config
import tender_spider.conn_db.test.save_data as save_data
import tender_spider.config
from tender_spider.get_data.test.get_data import get_data


def parser(response):

    soup = BeautifulSoup(response, 'lxml')

    # 公告名字
    name = soup('h1')[0].string
    print(name)

    # 内容url
    content_url = config.common_url + soup('script')[1].string.split('"')[1]

    print(content_url)

    # 获取详细信息
    result_data = get_data(content_url)

    content_soup = BeautifulSoup(result_data, 'lxml')

    # print(soup('table'))
    # print(soup('td')[0].string)

    # 解析详细内容
    content_data = ''
    # for i in content_soup('td'):

    for i in range(len(content_soup('td'))):
        # print(content_soup('td')[i].string)
        if not i == 0:
            content_data = content_data + '/ ' + str(content_soup('td')[i].string).replace(' ', '')
        else:
            content_data = str(content_soup('td')[i].string)

    print('公告详细信息')
    print(content_data)

    content_data_list=[]
    content_data_list.append(name)
    content_data_list.append(content_data)

    # 入库
    save_data.save_content_data(content_data_list)


