# -*- coding:UTF-8 -*-
import json
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup

'''
爬取智联招聘的信息
'''

class Zhilian(object):
    def __init__(self, kw, jl, start, end):
        self.kw = kw
        self.jl = jl
        self.start = start
        self.end = end
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        }
        # 智联网站
        self.url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?sm=0&'



    def handle_request(self, p):
        # 传递的参数
        data = {
            'kw':self.kw,
            'jl':self.jl,
            'p':p,
        }
        data = urllib.parse.urlencode(data)
        url = self.url+data
        request = urllib.request.Request(url=url,headers=self.headers)
        return request

    def download_data(self, request):
        items = []
        item={}
        response = urllib.request.urlopen(request)
        soup = BeautifulSoup(response.read(),'lxml')
        # 查找到所有的职位
        table_list = soup.select('#newlist_list_content_table .newlist')[1:]
        for table in table_list:
            #职位名称，公司名称，职位月薪，工作地点
            zwmc = table.select('.zwmc div a')[0].text
            gsmc = table.select('.gsmc a')[0].text
            zwyx = table.select('.zwyx')[0].text
            gzdd = table.select('.gzdd')[0].text
            item['zwmc'] = zwmc
            item['gsmc'] = gsmc
            item['zwyx'] = zwyx
            item['gzdd'] = gzdd
            items.append(item)
        string = json.dumps(items,ensure_ascii=False)
        with open('zhilian.txt','a',encoding='utf-8') as f:
            f.write(string)

    def run(self):
        for p in range(self.start,self.end+1):
            request = self.handle_request(p)
            self.download_data(request)

def main():
    kw = 'java'
    jl = '北京'
    start = 1
    end = 2
    obj = Zhilian(kw,jl,start,end)
    obj.run()


if __name__ == '__main__':
    main()
