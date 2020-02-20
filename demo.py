# encoding=utf8
# demo test for tender spider
# by hyn
# 20200106


import urllib.request
import simplejson

import requests

querystring = {"culture": "en-sg"}

payload = {'revAvailabilitySearch.SearchInfo.AdultCount': '1',
           'revAvailabilitySearch.SearchInfo.ChildrenCount': '0',
           'revAvailabilitySearch.SearchInfo.InfantCount': '0',
           'revAvailabilitySearch.SearchInfo.Direction': 'Oneway',
           'revAvailabilitySearch.SearchInfo.PromoCode': '',
           'revAvailabilitySearch.SearchInfo.SalesCode': '',
           'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureStationCode': 'SIN',
           'revAvailabilitySearch.SearchInfo.SearchStations[0].ArrivalStationCode': 'TPE',
           'revAvailabilitySearch.SearchInfo.SearchStations[0].DepartureDate': '03/30/2019',
           'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureStationCode': '',
           'revAvailabilitySearch.SearchInfo.SearchStations[1].ArrivalStationCode': '',
           'revAvailabilitySearch.SearchInfo.SearchStations[1].DepartureDate': '',
           'revAvailabilitySearch.DeepLink.OrganisationCode': '',
           'revAvailabilitySearch.DeepLink.Locale': '',

           }
headers = {
    # 'host': "makeabooking.flyscoot.com",
    # 'content-length': "831",
    # 'cache-control': "no-cache",
    # 'Origin': "http://qyn62.com",
    # 'upgrade-insecure-requests': "1",
    # 'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    # 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    # 'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    # 'Referer': "http://qyn62.com/details.html?label=MTQzMjU4MTk5OC5yc2MuY2RuNzcub3JnLzE1NDUyMjE0MDEvNDgwUF82MDBLXzE0NTUwNzQyMi5tM3U4&search=MjA1NQ==&name=JUU3JUJFJThFJUU1JUFFJUI5JUU5JTk5JUEyJUU4JTgwJTgxJUU2JTlEJUJGJUU1JUE4JTk4JUU3JTk2JUFGJUU3JThCJTgyJUU3JTk0JUJCJUU5JTlEJUEyJUU2JTgwJUE3JUU2JTg0JTlGJUU3JTk5JUJEJUU4JUExJUEzJUU4JUEzJTk5&label=JUU1JTlCJUJEJUU0JUJBJUE3JUUzJTgwJTgxJUU2JTgwJUE3JUU2JTg0JTlGJUU5JUJCJTkxJUU0JUI4JTlEJUUzJTgwJTgxJUU2JUI3JUFCJUU4JThEJUExJUU3JTg2JTlGJUU1JUE1JUIzJUUzJTgwJTgxJUU1JTgxJUI3JUU2JTgzJTg1",
    # 'accept-encoding': "gzip, deflate, br",
    # 'accept-language': "zh-CN,zh;q=0.9",
    # 'Cookie': "sId=581b9bb4c1ab4ae9ac44dd68be4c5ba2; SERVERID=652ffb8a9d83d5f9f7fe4e4ca4b6cd8a|1578289813|1578289810",
    # 'connection': "keep-alive",

}

# ip_proxies = {"https": "https://127.0.0.1:1080"}

# url = 'https://1432581998.rsc.cdn77.org/1545221401/480P_600K_145507422-0000.ts'
# response = requests.request("GET", url, data=payload,proxies=ip_proxies, headers=headers, params=querystring)
url = 'http://www.hngp.gov.cn/henan/list2?channelCode=0101&pageSize=16&bz=1&gglx=0&pageNo=1'
#response = requests.request("GET", url, headers=headers)
response = requests.request("GET", url, headers=headers)

# response=requests.get(url)
print(response.text)

