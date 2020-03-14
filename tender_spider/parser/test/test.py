# encoding=utf8
# 测试，获取公告数据
# by hyn
# 20200314

import tender_spider.parser.test.sample_parser as sample_parser
import tender_spider.parser.test.content_parser as content_parser
from tender_spider.get_data.test.get_data import get_data

# 获取简略信息
# url = 'http://www.hngp.gov.cn/henan/list2?channelCode=0101&pageSize=16&bz=1&gglx=0&pageNo=2'
# result_data=get_data(url)
# sample_parser.parser(result_data)

# 获取详细信息
url = 'http://www.hngp.gov.cn/henan/content?infoId=423717&channelCode=H600101'

# 获取详细地址，
result_data = get_data(url)
content_parser.parser(result_data)

# 获取公告详细信息

