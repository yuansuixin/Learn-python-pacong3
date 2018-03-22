# -*- coding:UTF-8 -*-
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p=1'

headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)

soup = BeautifulSoup(response.read(),'lxml')

table_list = soup.select('#newlist_list_content_table .newlist')[1:]

table_obj = table_list[0]
# print(table_obj)
zwmc = table_obj.select('.zwmc div a')[0].text
print(zwmc)
gsmc = table_obj.select('.gsmc a')[0].text
print(gsmc)
zwyx = table_obj.select('.zwyx')[0].text
print(zwyx)
gzdd = table_obj.select('.gzdd')[0].text
print(gzdd)