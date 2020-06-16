import scrapy

class Spider(scrapy.Spider):
    name = "web_spider"
    start_urls = ['https://vnexpress.net/']