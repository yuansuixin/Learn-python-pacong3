# -*- coding:UTF-8 -*-

from lxml import etree

tree = etree.parse('xpath.html')

print(tree)
ret = tree.xpath('//div[@class="haha"]/div[1]/a[last()]')[0].text
ret = tree.xpath('//div[@class="haha"]/div[1]/a/@href')[0]










