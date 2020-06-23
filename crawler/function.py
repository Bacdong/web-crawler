#!/usr/bin/python3
import requests
import psycopg2
from connection import openConnection
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

# insertDataCategories()


# insert data posts table
def insertDataPosts(*data):
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
    arrInsert = []
    index = 0
    for param in data:
        arrInsert.insert(index, str(param))
        index += 1
        # print('param: --------------------------------------- ', str(param))
        # dataLength += 1
    # print('Array Data: ========', arrInsert)

    query = """INSERT INTO posts(title, description, content, images, category_id) VALUES(%s, %s, %s, %s, %s)"""
    
    valuesInsert = (arrInsert)
    cur.execute(query, valuesInsert)
    connection.commit()

def checkCategory(category):
    categoryID = 0
    category = category.lower()

    if category == 'kinh doanh':
        categoryID = 1
    elif category == 'thời sự':
        categoryID = 2
    elif category == 'thế giới':
        categoryID = 3
    elif category == 'giải trí':
        categoryID = 4
    elif category == 'thể thao':
        categoryID = 5
    elif category == 'pháp luật':
        categoryID = 6
    elif category == 'giáo dục':
        categoryID = 7
    elif category == 'sức khỏe':
        categoryID = 8
    elif category == 'đời sống':
        categoryID = 9
    elif category == 'du lịch':
        categoryID = 10
    elif category == 'khoa học':
        categoryID = 11
    else:
        categoryID = 12

    return categoryID




# def findContent(data, typeFind, tagName, attr, valueAttr, getType):
#     return data.typeFind(tagName, {attr: valueAttr})getType

# def exportData(*data):
#     captions = ["Category: ", "Title: ", "Description: ", "Content: ", "URL Image: "]
#     index = 0
#     for param in data:
#         for caption in captions:
#             print(index, '.', caption, param, '\n\n')
#             index += 1