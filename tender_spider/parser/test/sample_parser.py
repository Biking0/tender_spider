# encoding=utf8
# 解析公告简略信息
# by hyn
# 20200308


import urllib.request
import simplejson
from bs4 import BeautifulSoup
import requests
from lxml import etree
import tender_spider.config as config
import tender_spider.conn_db.test.save_data as save_data


def parser(response):
    # print()
    soup = BeautifulSoup(response, 'lxml')

    url_list = soup.find('div', attrs={'class': 'List2'}).find_all('li')  # 找到class="wrap"的div里面的所有<img>标签

    # 公告简略信息列表
    # print(url_list)
    # print(url_list[0])
    # print(type(url_list[0]))
    # print(url_list[0]('a'))

    # 存储公告简略信息，入库
    sample_info_list = []

    # 获取简略信息
    for sample_info in url_list:
        # 公告简略信息字段对应
        sample_info_data = []
        name = sample_info('a')[0].string
        company = sample_info('span')[1].string
        view_cont = sample_info('span')[3].string
        release_time = sample_info('span')[4].string
        url = config.common_url + sample_info('a')[0]['href']

        sample_info_data.append(name)
        sample_info_data.append(company)
        sample_info_data.append(view_cont)
        sample_info_data.append(release_time)
        sample_info_data.append(url)

        print(sample_info_data)

        sample_info_list.append(sample_info_data)
        # break

    # 入库
    save_data.save_sample_data(sample_info_list)
    return sample_info_list
