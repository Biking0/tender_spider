# encoding=utf8
# 解析公告详细信息
# by hyn
# 20200308


import urllib.request
import simplejson
from bs4 import BeautifulSoup
import requests
from lxml import etree
import tender_spider.config as config
import tender_spider.conn_db.test.save_data as save_data
import tender_spider.config
from tender_spider.get_data.test.get_data import get_data


def parser(response):
    # 修改编码

    # print(response)
    # response=response.encode(encoding='utf-8')

    # print()
    soup = BeautifulSoup(response, 'lxml')

    # 公告名字
    name = soup('h1')[0].string
    print(name)

    # 内容url
    content_url = config.common_url + soup('script')[1].string.split('"')[1]

    # for i in soup('script')[1].string.split('"'):
    #     print(i)
    #     print('##############')

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

    # url_list = soup.find('div', attrs={'class': 'List2'}).find_all('li')  # 找到class="wrap"的div里面的所有<img>标签
    #
    # # 公告简略信息列表
    # # print(url_list)
    # print(url_list[0])
    # # print(type(url_list[0]))
    # # print(url_list[0]('a'))
    #
    # # 存储公告简略信息，入库
    # sample_info_list = []
    #
    # # 获取简略信息
    # for sample_info in url_list:
    #     # 公告简略信息字段对应
    #     sample_info_data = []
    #     name = sample_info('a')[0].string
    #     company = sample_info('span')[1].string
    #     view_cont = sample_info('span')[3].string
    #     release_time = sample_info('span')[4].string
    #     url = config.common_url + sample_info('a')[0]['href']
    #
    #     sample_info_data.append(name)
    #     sample_info_data.append(company)
    #     sample_info_data.append(view_cont)
    #     sample_info_data.append(release_time)
    #     sample_info_data.append(url)
    #
    #     print(sample_info_data)
    #
    #     sample_info_list.append(sample_info_data)
    #
    #     # break
    #
    # sample_info_list
    #
    # # 入库
    # save_data.save_data(sample_info_list)
