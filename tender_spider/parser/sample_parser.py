# encoding=utf8
# 解析公告简略信息
# by hyn
# 20200308


import urllib.request
import simplejson
from bs4 import BeautifulSoup
import requests
from lxml import etree


def parser(response):
    # print()
    soup = BeautifulSoup(response, 'lxml')
    # test=soup.find_all(attrs={"class": "List2"})  #也可以通过字典的方式查找

    # div=soup('div')

    url_list = soup.find('div', attrs={'class': 'List2'}).find_all('li')  # 找到class="wrap"的div里面的所有<img>标签

    # 公告简略信息列表
    print(url_list)
    print(url_list[0])

    tree = etree.HTML(response)

    div_text = tree.xpath('//div[@class="List2"]//li//text()')

    print(div_text)
    print(div_text[0])
    print(type(div_text[0]))

    div = tree.xpath('//div[@class="List2"]//li')


