# import urllib.request

# def crawl(url):
#     links = analyze(url)
#     for link in links:
#         try:
#             crawl(link)
#         except:
#             pass

# def analyze(url):
#     print('Visiting', url)
#     content = urllib.request.urlopen(url)
#     socket = content.read().decode()
#     collector = Collector(url)
#     collector.feed(content)
#     urls = collector.getLinks()
#     return urls

# from urllib.parse import urljoin
# from html.parser import HTMLParser
# class Collector(HTMLParser):
# 'collects hyperlink URLs into a list' def __init__(self, url):
# 'initializes parser, the url, and a list'
# HTMLParser.__init__(self)
# self.url = url
# self.links = []

# def handle_starttag(self, tag, attrs):
# 'collect hyperlink URLs in their absolute format'
# if tag == 'a':pip install scrapy
# for attr in attrs:
# if attr[0] == 'href':
# # construct absolute URL
# absolute = urljoin(self.url, attr[1])
# if absolute[:4] == 'http': # collect HTTP URLs
# self.links.append(absolute)

# def getLinks(self):
# 'returns hyperlinks URLs in their absolute format'
# return self.links

# url = 'https://vnexpress.net/'
# crawl(url)

print('Hello World')