# encoding=utf8
# 生成简略信息url池，请求网络，调用简略信息解析，调用详细信息，
# by hyn
# 20200322
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')
from bs4 import BeautifulSoup
import tender_spider.config as config
from tender_spider.get_data.test.get_data import get_data
import re


# 获取总页数，省级总页数
def pro_totalpage():
    response = get_data(config.pro_url)

    soup = BeautifulSoup(response, 'lxml')

    pro_totalpage_str = soup.find('li', attrs={'class': 'pageInfo'}).string.replace(' ', '')

    pro_totalpage = int(re.findall("\d+", pro_totalpage_str)[0])
    print(pro_totalpage)
    return pro_totalpage


# 市区县总页数
def city_totalpage():
    response = get_data(config.city_url)

    soup = BeautifulSoup(response, 'lxml')

    city_totalpage_str = soup.find('li', attrs={'class': 'pageInfo'}).string.replace(' ', '')

    city_totalpage = int(re.findall("\d+", city_totalpage_str)[0])
    print(city_totalpage)
    return
