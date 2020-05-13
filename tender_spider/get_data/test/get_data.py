# encoding=utf8
# 请求网站，获取数据
# by hyn
# 20200314

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')

import requests
import time
import random
from fake_useragent import UserAgent


# 通用网络请求方法
def get_data(url):
    try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        response = requests.request("GET", url, headers=headers)

        return response.content
    except Exception as e:
        time.sleep(random.randint(5, 20))

        print(e)
