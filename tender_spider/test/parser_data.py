# encoding=utf8
# 测试，解析公告简略信息
# by hyn
# 20200106


import urllib.request
import simplejson
from bs4 import BeautifulSoup
import requests

from lxml import etree
import requests


# res=requests.get('http://www.w3school.com.cn/')
# tree=etree.HTML(res.content)
# div=tree.xpath('//div[@id="d1"]')[0]
# div_str=etree.tostring(div,encoding='utf-8')
# print div_str


def parser(response):
    # print()
    soup = BeautifulSoup(response, 'lxml')
    # test=soup.find_all(attrs={"class": "List2"})  #也可以通过字典的方式查找

    # div=soup('div')

    url_list = soup.find('div', attrs={'class': 'List2'}).find_all('li')  # 找到class="wrap"的div里面的所有<img>标签

    # 公告简略信息列表
    print(url_list)
    print(url_list[0])

    # print(url_list[0].attrs['href'])
    # print(url_list[0].get_text())

    # url_list=soup.find('div', attrs={'class': 'List2'}).find_all('a') # 找到class="wrap"的div里面的所有<img>标签
    #
    # # url_list
    # print(url_list[0].attrs['href'])
    # print(url_list[0].get_text())
    # print(reuslt)

    # soup.
    # print(test[0])
    # print(test[0]('li'))
    # test=soup('div')

    # print(test)

    tree = etree.HTML(response)

    div_text = tree.xpath('//div[@class="List2"]//li//text()')

    print(div_text)
    print(div_text[0])
    print(type(div_text[0]))

    div = tree.xpath('//div[@class="List2"]//li')

    # print(div)
    # print(div[0])
    # print(type([0]))
    #
    # div_str = etree.tostring(div[0])
    # print(div_str)
    # print(soup.find())
