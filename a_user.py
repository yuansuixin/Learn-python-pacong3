# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup


soup = BeautifulSoup(open('test.html',encoding='utf-8'),'lxml')

a_obj = soup.a
# print(a_obj.name)
# print(a_obj.attrs)
# print(a_obj.attrs['href'])
# print(a_obj['href'])


# print(a_obj.string)
# print(a_obj.get_text())
# print(a_obj.text)

# div_obj = soup.div
#
# lt=['\n','\n','a','b']
# print(div_obj.contents)
# print(list(div_obj.descendants))#返回的是一个生成器

a_obj = soup.find('a')
a_obj = soup.find('a',id='dufu')
a_obj = soup.find('a',{'class':'juyi','id':'libai'})
# 返回的是一个对象列表
a_obj = soup.find_all('a')
#注意使用class属性的时候需要加上一个_下划线
a_obj = soup.find_all('a',class_='juyi')
# 找到所有的a和li
a_obj = soup.find_all(['a','li'])
#找到前两个a
a_obj = soup.find_all('a',limit=2)

# css选择器
a_list = soup.find_all('div a')
a_obj = a_list[0]
print(a_obj.select('div b'))






