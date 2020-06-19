#!/usr/bin/python3
import requests
import psycopg2
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

# Example:
# tableName = 'category'
# values = "2, 'Kinh Doanh'"
def insertDataCategories():
    serverName = 'localhost'
    username = 'postgres'
    password = 'Faker1412'
    dbName = 'WebCrawler'

    connection = psycopg2.connect(
        host = serverName, 
        database = dbName, 
        user = username, 
        password = password
    )

    cur = connection.cursor()
    query = """INSERT INTO categories(id, name) VALUES(%s, %s)"""
    valuesInsert = (1, 'Kinh Doanh')
    cur.execute(query, valuesInsert)
    connection.commit()

insertDataCategories()


# def findContent(data, typeFind, tagName, attr, valueAttr, getType):
#     return data.typeFind(tagName, {attr: valueAttr})getType

# def exportData(*data):
#     captions = ["Category: ", "Title: ", "Description: ", "Content: ", "URL Image: "]
#     index = 0
#     for param in data:
#         for caption in captions:
#             print(index, '.', caption, param, '\n\n')
#             index += 1