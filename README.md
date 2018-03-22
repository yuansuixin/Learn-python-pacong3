# Learn-python-pacong3

- 爬虫学习时候的练习
- 爬取了智联招聘的信息



### 知识点

day04-爬虫4

- bs4(beautifulsoup)
	其给我们提供的接口非常的人性化，人性化的意思就是可以通过以前学习的css选择器来选择你想要的内容，相对来说，用的简单的东西，效率稍微的低一点，相对xpath来说低
	bs4就是一个网页解析器，通过选择器来提取你想要的内容
	安装
		pip进行安装
		pip源切换为国内源，豆瓣源、阿里源
			windows
				打开文件管理器， %appdata%
				在这里面新建一个文件夹  pip
				在pip文件夹里面新建一个文件叫做  pip.ini
				粘贴如下内容
					[global]
					timeout = 6000
					index-url = https://mirrors.aliyun.com/pypi/simple/
					trusted-host = mirrors.aliyun.com
			linux
				mkdir ~/.pip           新建一个目录
				vi ~/.pip/pip.conf     编辑pip配置文件
				将上面的内容粘贴进来即可
		pip install lxml   用来解析html内容的库
		pip install bs4    bs4支持的api库
	使用
		导入库
			from bs4 import BeautifulSoup
			先通过BeautifulSoup生成一个对象，然后根据对象的方法去提取里面的元素
			通过网页内容或者本地内容来生成对象
			soup = BeautifulSoup(网上下载的内容字符串或者字节, 'lxml')
			soup = BeautifulSoup(open('本地文件名'), 'lxml')
			sublime好用的插件
		标签名查找
			查找的永远是第一个标签
			得到的是一个对象
		节点的属性
			a_obj.name  获取标签名
			a_obj.attrs 获取该标签对象所有属性，以键值对字典形式返回给你
		获取节点属性值（常用）
			a_obj.attrs['href']
			a_obj['href']
			a_obj.get('href')
		获取节点内容（常用）
			a_obj.string
			a_obj.text
			a_obj.get_text()
			【注】如果标签里面还有标签，使用的时候，尽量使用后两个，因为string获取为空，text和get_text()可以获取纯字符内容
		获取直接子节点（基本不用）
			contents
			返回一个列表
			获取的直接子节点有换行符
		获取子孙节点（基本不用）
			descendants
			返回一个生成器
			获取所有的子孙节点，有换行符
		方法（常用）
			find(返回对象)
				find('a')  找到第一个a
				如下案例，根据属性有针对性的去查找。找到的是符合要求的第一个元素
				find('a', title='xxx')
				find('a', class_='xxx')  
				find('a', {'class': 'juyi', 'id': 'dufu'})
			find_all(返回列表,列表里面都是满足要求的节点对象)
				find_all('a')  得到所有的a
				find_all('a', class_='juyi')  满足要求所有的a
				find_all(['a', 'li'])  找到所有的a和li
				find_all('a', limit=2) 找到前两个a
			select(常用的) 返回一个列表,列表中都是符合要求的节点对象，通过对象的方法再去获取对象属性值或者节点值
				标签选择器
				类选择器    .baby
				id选择器    #baby
				层级选择器  
					div span a      没有层级限制
					div > span > a  必须是子节点
					.baby > #hello a > .haha
				属性选择器
					input[type='checkbox']
			【注】列表中的对象，可以接着使用select进行查找
      
- xpath
	<code></code>
	语法学习
		什么是xml
		什么是xpath
			就是一种路径表达式，对xml里面的元素或者属性进行查找
			由于html就是一种特殊的xml，所以xpath就能从html提取出来指定的元素
			常用的路径表达式
			/  从根路径开始查找
				也可以作为层级分隔符，表示后一个节点是前一个节点的直接子节点
			// 从任意位置开始查找
			.  从当前节点开始查找
			.. 当前节点的父节点
			@  选取属性节点

			bookstore/book
				这个是查找bookstore节点下面所有的直接子节点book
			bookstore//book
				这个是查找bookstore里面任意子节点book
			/bookstore/book[1]
				取出bookstore里面的第一个book，注意，下标从1开始，而不是从0开始
			/bookstore/book[last()]
				取出bookstore里面的最后一个book
			/bookstore/book[last()-1]
				取出bookstore里面的倒数第二个book
			/bookstore/book[position()<3]
				取出bookstore里面的前两个book
			//title[@lang]
				查询所有具有lang属性的title节点
			//title[@lang='eng']
				查询所有lang属性值为eng的title节点
			/bookstore/*
				查询bookstore下面所有的节点
			//book/title | //book/price
				或者的关系，满足一条即可
		安装xpath插件
			谷歌浏览器===》右上角三个点==》更多工具===》扩展程序，将xpath.crx文件拖进来安装即可
			使用： ctrl + shift + x
			取消:  ctrl + shift + x
		属性定位
			查找属性值等于su的input节点
			//input[@id="su"]
		层级定位
			//div[@class="head_wrapper"]/div[@class="s_form"]/div/form/span[@class="bg s_btn_wr"]/input
			【注1】xpath路径表达式查找到的不止一个满足要求的节点，所以应该返回一个列表
			【注2】如果通过class进行限制，class有几个就要写几个
			//div[@class="head_wrapper"]/div[@class="s_form"]//input[@class="bg s_btn"]
			也可以直接写到半路，来一个双斜杠，通过限制进行查找
		索引定位
			# 指定div下面所有a
			//div[@class="s_tab"]/a
			# 指定div下面第一个a
			//div[@class="s_tab"]/a[1]
			# 指定div下面最后一个a
			//div[@class="s_tab"]/a[last()]
			# 指定div下面倒数第二个a
			//div[@class="s_tab"]/a[last()-1]
			# 指定div下面的第2个div下面的第三个a
			//div[@id="wrapper"]/div[2]/a[3]
		逻辑运算
			and   两个条件同时满足才能查找得到
			//div[@id="s_tab" and @class="s_tab"]
		模糊匹配
			contains函数
			查找指定条件的a，a的属性wdfield，其属性值包含k的所有a
			//div[@id="s_tab"]/a[contains(@wdfield, "k")]

			starts-with函数
			属性值以k开头的所有满足条件的a
			//div[@id="s_tab"]/a[starts-with(@wdfield, "k")]
		取文本
			获取第二个a的文本内容
			//div[@id="s_tab"]/a[2]/text()
		取属性
			//div[@id="s_tab"]/a[1]/@href
		从谷歌浏览器中自动copy xpath
		//*[@id="s_tab"]/a[1]
		【注】谷歌copy的xpath，还有自己写的xpath都仅供参考，只有在代码中真正能获取到结果的xpath，才是最可信的xpath
	安装模块
		pip install lxml
	代码中使用
		（1）读取本地内容生成对象
		from lxml import etree
		tree = etree.parse('test.html')
		ret = tree.xpath('xxx')
		获取得到的ret是一个列表
		如果xpath精确到节点
			那么列表中存放的就都是对象
			对象.text  可以获取文本内容
		如果xpath精确到属性或者文本
			那么列表中存放就都是字符串
		（2）通过网络响应内容生成对象
