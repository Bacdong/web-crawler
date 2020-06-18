import requests
from bs4 import BeautifulSoup

def getData(url, tagName, className):
    res = requests.get(url)

    if res.status_code != 200:
        print('Get Data Failed!')
    else:
        detailed_soup = BeautifulSoup(res.content, "html.parser")
        result = detailed_soup.find(tagName, {"class": className})
        return result

def getURLNewsLatest(newsLatest):
    return newsLatest.find("a", {"class": "thumb thumb-5x3"})["href"]

# def findContent(data, typeFind, tagName, attr, valueAttr, getType):
#     return data.typeFind(tagName, {attr: valueAttr})getType

# def exportData(*data):
#     captions = ["Category: ", "Title: ", "Description: ", "Content: ", "URL Image: "]
#     index = 0
#     for param in data:
#         for caption in captions:
#             print(index, '.', caption, param, '\n\n')
#             index += 1