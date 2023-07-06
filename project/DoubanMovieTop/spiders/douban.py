import scrapy
import csv
import pymysql

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = ['https://movie.douban.com/top250']

    def __init__(self):
        self.item_buffer = []
        # 新增：连接MySQL数据库
        self.db = pymysql.connect(
            host="localhost", user="root", password="12345678",database="douban"
        )

    def parse(self, response):
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item = {}
            item['ranking'] = movie.xpath('.//div[@class="pic"]/em/text()').extract()
            item['movie_name'] = movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()
            item['score'] = movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()
            item['score_num'] = movie.xpath('.//div[@class="star"]/span/text()').re(
                r'(\d+)人评价')
            self.item_buffer.append(item)

        next_url = response.xpath('//span[@class="next"]/a/@href')
        if next_url:
            yield response.follow(next_url[0], self.parse)
        else:
            yield {'items': self.item_buffer}

    def closed(self, reason):
        items = self.crawler.stats.get_value('item_scraped_count')
        filename = 'output.csv'
        with open(filename, 'w', newline='', encoding="utf_8_sig") as f:
            writer = csv.writer(f)
            writer.writerow(['Ranking', 'Name', 'Score', 'Number of Scores'])
            for item in self.item_buffer:
                writer.writerow([item['ranking'][0], item['movie_name'][0], item['score'][0], item['score_num'][0]])
        
        # 新增：将数据插入MySQL数据库中
        cursor = self.db.cursor()
        cursor.execute("TRUNCATE TABLE movies")
        for item in self.item_buffer:
            sql = "INSERT INTO movies (ranking, movie_name, score, score_num) VALUES (%s, %s, %s, %s)"
            val = (item['ranking'][0], item['movie_name'][0], item['score'][0], item['score_num'][0])
            cursor.execute(sql, val)
        self.db.commit()

    # 新增：查询数据库中的数据
    def query(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM movies")
        result = cursor.fetchall()
        for row in result:
            print(row)
