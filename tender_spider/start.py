# encoding=utf8
# 爬虫启动器
# by hyn
# 20200322


import os
import sys

# 尽量将项目放到D盘根目录，否则下面路径为实际项目路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')
sys.path.append('D:/project/github/tender_spider')
sys.path.append('D:/tender_spider')

from tender_spider.main import main

if __name__ == "__main__":
    main.main()
