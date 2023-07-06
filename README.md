# Python-Scrapy-DoubanMovieTop250
1.创建新的Scrapy项目；2.定义要爬取的网站；3.创建一个Spider类；4.编写Spider的解析方法；5.定义数据存储方式；6.启动爬虫；7.数据提取后，将数据写入MySQL数据库中。

## 具体要求

1.创建新的Scrapy项目：使用“Scrapy startproject”命令创建一个新的Scrapy项目。
2.定义要爬取的网站：在项目目录下的settings.py文件中定义要爬取的网站。
3.创建一个Spider类：使用“Scrapy genspider”命令创建一个新的spider类，定义爬取的URL。
4.编写Spider的解析方法：在Spider类中编写解析方法，用来提取网页中的数据。
5.定义数据存储方式：可以使用Scrapy提供的各种数据存储方式,如保存到CSV文件。
6.启动爬虫：使用“Scrapy crawl”命令启动爬虫。Scrapy会自动下载网页，提取数据，并按照定义好的数据存储方式将数据保存下来。定义好的数据存储方式将数据保存下来。
7.数据提取后，将数据写入MySQL数据库中进行存储生成.db文件并能够执行展示或查询操作。

# 1 项目背景

随着信息化的快速发展，数据已经成为现代社会的基石之一。在当今数字化时代，豆瓣电影TOP250作为最具人气和知名度的电影排行榜之一，拥有着极高的实用价值和分析意义。本项目旨在使用Python编程语言，结合网络爬虫技术，对豆瓣电影TOP250进行数据爬取并存储到数据库中。通过对电影各类数据的爬取和存储，可以为广大电影观众和市场分析师提供可靠的市场参考和数据统计。本项目将由一个小组的六名成员共同合作完成，每个成员都将承担不同的责任和任务。

小组成员中的项目背景负责人将负责整个项目背景的调研和分析，确认项目的目的和相关技术资料，并协助团队成员进行任务规划和进度安排。Python技术负责人将选取合适的编程语言和技术用于实现爬虫和数据存储。开发工具负责人将选择并熟练掌握开发工具，确保整个项目的开发过程更加高效和顺利。爬虫和数据库分析负责人将分析和确定爬虫方法和数据库的实现方法，为整个小组提供技术支持和建议。爬虫实现程序分析负责人将分析和评估爬虫程序的实现，并提出改进建议。数据库创建及查询实现负责人将管理数据库、设计数据库表结构和编写SQL查询语句，以确保数据能够被正确存储和检索。优化分析负责人将监控和改进系统性能，从而提升整个系统的效率和响应速度。

# 2 项目技术——Python 3

Python是一种高级编程语言，具有简单易学、跨平台、可扩展性和开放源代码等特点。在当今大数据分析和人工智能领域，Python已成为最常用的编程语言之一，其强大的生态系统和丰富的库使得它成为了数据科学家、软件工程师和网站开发者的首选。

在本项目中，我们选择使用Python 3作为项目的主要编程语言。Python 3相比于Python 2，有一些显著改进，如支持Unicode字符串和语法上的改进等。Python 3还具有更好的兼容性和稳定性，在性能和安全性方面也有所提升。因此，我们选择使用Python 3来保障项目的开发效率与质量。

Python 3在爬虫和数据存储方面也有着广泛的应用。Python的Scrapy框架是一种强大的网络爬虫框架，可以实现高效的数据爬取和处理。在本项目中，我们采用Scrapy框架来实现豆瓣电影TOP250的数据爬取，利用XPath对HTML文件进行解析和数据清洗。同时，Python 3也具有优秀的数据库操作库，如pymysql等，使得Python能够很容易地连接到数据库服务器，并对数据进行增删改查等操作。在本项目中，我们使用MySQL数据库作为数据存储的工具，通过Python 3的数据库API来连接和操作MySQL数据库。

Python 3还有许多强大的第三方库，如Numpy、Pandas和Matplotlib等，能够帮助我们更快地进行数据分析和可视化，并提高代码的运行效率。此外，Python 3的生态系统非常丰富，有着众多的文档、教程、社区和工具支持，因此我们可以更快速地解决问题，提高项目开发的效率和质量。

综上所述，Python 3是一种高效、易学、可扩展、且强大的编程语言，其在爬虫和数据存储方面具有广泛应用。在本项目中，我们选择使用Python 3作为主要的编程语言，结合Scrapy框架和MySQL数据库，实现豆瓣电影TOP250的数据爬取和存储，目标是为电影观众和市场分析师提供可靠的市场参考和数据统计。

# 3 开发工具——Scrapy框架

Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 其可以应用在数据挖掘，信息处理或存储历史数据等一系列的程序中。

其最初是为了页面抓取 (更确切来说, 网络抓取 )所设计的， 也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。Scrapy 使用了 Twisted异步网络库来处理网络通讯。整体架构大致如下

## 3.1 Scrapy主要组件

引擎(Scrapy)：用来处理整个系统的数据流处理, 触发事务(框架核心)

调度器(Scheduler)：用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想象成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址

下载器(Downloader)：用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)

爬虫(Spiders)：爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面

项目管道(Pipeline)：负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。

下载器中间件(Downloader Middlewares)：位于Scrapy引擎和下载器之间的框架，主要是处理Scrapy引擎与下载器之间的请求及响应。

爬虫中间件(Spider Middlewares)：介于Scrapy引擎和爬虫之间的框架，主要工作是处理蜘蛛的响应输入和请求输出。

调度中间件(Scheduler Middewares)：介于Scrapy引擎和调度之间的中间件，从Scrapy引擎发送到调度的请求和响应。

## 3.2 Scrapy运行流程

引擎从调度器中取出一个链接(URL)用于接下来的抓取

引擎把URL封装成一个请求(Request)传给下载器

下载器把资源下载下来，并封装成应答包(Response)

爬虫解析Response

解析出实体（Item）,则交给实体管道进行进一步的处理

解析出的是链接（URL）,则把URL交给调度器等待抓取

## 3.3 Scrapy常用命令

scrapy startproject <爬虫名称> 创建爬虫名称（唯一）

scrapy genspider<爬虫项目名称> 创建爬虫项目名称

scrapy list 列出所有爬虫名称

scrapy crawl <爬虫名称> 运行爬虫

# 4爬虫及数据储存分析

## 4.1 爬虫方法分析

首先，在创建Scrapy项目后，我们使用scrapy genspider命令创建一个名为“douban”的爬虫类，并在其中定义了起始URL(https://movie.douban.com/top250)：

class DoubanSpider(scrapy.Spider):

  name = 'douban'

  start_urls = ['https://movie.douban.com/top250']

在爬虫类中，我们通过parse()方法来处理响应，并从中抓取电影信息。使用XPath选择器，我们可以轻松地定位所需元素的位置。这里，我们使用了response.xpath()方法和相关的XPath表达式来抓取电影排名、电影名称、电影评分和电影评论数。

def parse(self, response):

​    movies = response.xpath('//ol[@class="grid_view"]/li')

​    for movie in movies:

​      item = {}

​      item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()

​      item['movie_name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()

​      item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()

​      item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(

​        r'(\d+)人评价')

​      self.item_buffer.append(item)

在这里，我们使用了extract()和re()方法来提取元素文本或正则表达式匹配结果。将抓取到的数据存入名为“item”的字典中，并将其保存到self.item_buffer列表中。

接着，我们使用response.follow()方法来判断是否存在下一页并继续访问页面，并在else语句块中将抓取到的数据保存到CSV文件中。

next_url = response.xpath('//span[@class="next"]/a/@href')

if next_url:

  yield response.follow(next_url[0], self.parse)

else:

  yield {'items': self.item_buffer}

最后，在closed()方法中，我们将爬取到的数据插入MySQL数据库，并且将其保存到CSV文件中。这里，我们使用了pymysql库来连接数据库，并在循环中对每个电影记录执行一次INSERT语句操作。

def closed(self, reason):

  items = self.crawler.stats.get_value('item_scraped_count')

  filename = 'output.csv'

  with open(filename, 'w', newline='', encoding="utf_8_sig") as f:

​    writer = csv.writer(f)

​    writer.writerow(['Ranking', 'Name', 'Score', 'Number of Scores'])

​    for item in self.item_buffer:

​      writer.writerow([item['ranking'][0], item['movie_name'][0], item['score'][0], item['score_num'][0]])

  \# 新增：将数据插入MySQL数据库中

  cursor = self.db.cursor()

cursor.execute("TRUNCATE TABLE movies")

  for item in self.item_buffer:

​    sql = "INSERT INTO movies (ranking, movie_name, score, score_num) VALUES (%s, %s, %s, %s)"

​    val = (item['ranking'][0], item['movie_name'][0], item['score'][0], item['score_num'][0])

​    cursor.execute(sql, val)

  self.db.commit()

如果需要查询数据库中的数据，可以调用query()方法来查询。这里，我们使用了cursor.execute()方法执行SELECT语句，并使用fetchall()方法获取所有记录，最后通过循环遍历输出结果。

\# 新增：查询数据库中的数据

def query(self):

  cursor = self.db.cursor()

  cursor.execute("SELECT * FROM movies")

  result = cursor.fetchall()

  for row in result:

​    print(row)

## 4.1 数据库实现方法分析

首先，我们导入pymysql库并使用其中的connect()方法连接到MySQL数据库。在连接过程中，需要指定主机地址、用户名、密码和数据库名称等参数。

from pymysql import connect

 

db = connect(

  host="localhost",

  user="root",

  password="12345678",

  database="douban"

)

接下来，我们创建了一个游标对象cursor，并使用execute()方法来执行查询SQL语句。这里，我们使用了SELECT * FROM movies语句来查询电影表中的所有记录，并使用fetchall()方法将查询结果存储在result变量中。

cursor = db.cursor()

cursor.execute("SELECT * FROM movies")

result = cursor.fetchall()

最后，我们通过循环遍历result变量来输出查询结果。

for row in result:

  print(row)

最后，在程序结束时，我们需要关闭数据库连接以释放资源。

db.close()

 

# 5爬取实现程序——豆瓣电影TOP250

## 5.1 利用scrapy库和正则表达式来抓取猫眼电影TOP100的相关内容

爬取目标：电影排名、电影名称、电影评分、电影评论数

创建新的Scrapy项目：使用“Scrapy startproject”命令创建一个新的Scrapy项目。创建一个Spider类：使用“Scrapy genspider”命令创建一个新的spider类，定义爬取的URL。

scrapy startproject DoubanMovieTop

cd DoubanMovieTop

scrapy genspider douban

 

修改默认“user-agent”和reboots为True

修改settings.py文件以下参数：

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'

ROBOTSTXT_OBEY = False

 

Item使用简单的class定义语法以及Field对象来声明。

写入下列代码声明Item

import scrapy

class DoubanmovietopItem(scrapy.Item):

  ranking = scrapy.Field()#排名

  movie_name = scrapy.Field()#电影名称

  score = scrapy.Field()#评分

  score_num = scrapy.Field()#评论人数

 

分析网页源码抓取所需信息

import scrapy

import csv

import pymysql

class DoubanSpider(scrapy.Spider):

  name = 'douban'

  start_urls = ['https://movie.douban.com/top250']

  def __init__(self):

​    self.item_buffer = []

​    \# 新增：连接MySQL数据库

​    self.db = pymysql.connect(

​      host="localhost",user="root",password="12345678",database="douban"

​    )

  def parse(self, response):

​    movies = response.xpath('//ol[@class="grid_view"]/li')

​    for movie in movies:

​      item = {}

​      item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()

​      item['movie_name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()

​      item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()

​      item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(

​        r'(\d+)人评价')

​      self.item_buffer.append(item)

​    next_url = response.xpath('//span[@class="next"]/a/@href')

​    if next_url:

​      yield response.follow(next_url[0], self.parse)

​    else:

​      yield {'items': self.item_buffer}

  def closed(self, reason):

​    items = self.crawler.stats.get_value('item_scraped_count')

​    filename = 'output.csv'

​    with open(filename, 'w', newline='', encoding="utf_8_sig") as f:

​      writer = csv.writer(f)

​      writer.writerow(['Ranking', 'Name', 'Score', 'Number of Scores'])

​      for item in self.item_buffer:

​        writer.writerow([item['ranking'][0], item['movie_name'][0], item['score'][0], item['score_num'][0]])

​    \# 新增：将数据插入MySQL数据库中

​    cursor = self.db.cursor()

​    for item in self.item_buffer:

​      sql = "INSERT INTO movies (ranking, movie_name, score, score_num) VALUES (%s, %s, %s, %s)"

​      val = (item['ranking'][0], item['movie_name'][0], item['score'][0], item['score_num'][0])

​      cursor.execute(sql, val)

​    self.db.commit()

  \# 新增：查询数据库中的数据

  def query(self):

​    cursor = self.db.cursor()

​    cursor.execute("SELECT * FROM movies")

​    result = cursor.fetchall()

​    for row in result:

​      print(row)

 

运行爬虫

scrapy crawl douban

 

打开excel表格和数据库查看抓取结果。



 

## 5.2 数据库创建及查询实现

check.py查询数据库程序设计

from pymysql import connect

\# 连接数据库

db = connect(

  host="localhost",

  user="root",

  password="12345678",

  database="douban"

)

\# 查询所有电影信息

cursor = db.cursor()

cursor.execute("SELECT * FROM movies")

result = cursor.fetchall()

\# 打印结果

for row in result:

  print(row)

\# 关闭连接

db.close()



 

# 6优化分析

  本项目使用Scrapy框架实现了豆瓣电影TOP250的数据爬取，包括电影排名、电影名称、电影评分、电影评论数等信息，并将数据存储在CSV文件和MySQL数据库中。在进行爬取过程中，我们可以从以下两个方面对其进行优化。

  一、XPath解析器的优化

  XPath是Scrapy中用于解析HTML或XML文档的语言，它具有高度的灵活性和可扩展性，但其在性能方面略逊于CSS选择器。因此，在进行XPath解析时，可以优先考虑使用CSS选择器，以提高代码的运行效率。同时，在编写XPath表达式时，应该尽量避免使用通配符“//”和“*”，因为这些通配符会增加解析文档的时间和复杂度，从而影响代码的执行效率。

  二、爬虫程序的优化

  在爬虫程序中，我们可以进行以下优化：

  增加请求间隔时间，避免对服务器造成过大的压力。

  利用“yield”关键字确保代码的异步执行，避免代码阻塞导致爬虫程序失效。

  使用数据库连接池技术，避免进行频繁的数据库连接和断开操作，从而提高代码的执行效率。

  对爬取数据进行清洗和过滤，避免无用数据的存储和传输，提高代码的性能和可靠性。

  综上所述，本项目使用Scrapy框架实现了豆瓣电影TOP250的数据爬取，并将数据存储在CSV文件和MySQL数据库中。在进行优化时，我们可以从XPath解析器的优化和爬虫程序的优化两个方面入手，以提高代码的运行效率和性能。



