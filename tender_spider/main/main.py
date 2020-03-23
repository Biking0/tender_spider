# encoding=utf8
# 爬虫主函数
# by hyn
# 20200322


# 构造url，根据url获取书数据，调用简略解析，调用详细解析
from tender_spider.url_pool import url_pool  as url_pool
import tender_spider.config as config
from tender_spider.get_data.test.get_data import get_data
import tender_spider.parser.test.sample_parser as sample_parser
import tender_spider.parser.test.content_parser as content_parser


# 构造url，根据url获取书数据，调用简略解析，调用详细解析
def main():
    pro_totalpage=url_pool.pro_totalpage()
    city_totalpage=url_pool.city_totalpage()

    print('开始爬取，总页数：',pro_totalpage)
    for i in range(1,pro_totalpage):
        url=config.pro_page_url+str(i)
        print('正在爬取，第',i,'页',url)
        response=get_data(url)
        sample_parser.parser(response)



