#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import psycopg2
import re
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
    arrCurrentData = getDataFromDB()
    print('array Data', arrCurrentData)

    arrInsert = []
    index = 0
    for param in data:
        for dataCate in arrCurrentData:
            if (param != dataCate):
                print('Data cate: ', dataCate, '\n')
                print('Input cate: ', param, '\n')
                print('Can save')
                arrInsert.insert(index, str(param))
            else:
                print('Data cate: ', dataCate, '\n')
                print('Input cate: ', param, '\n')
                print('Cannot save')
        index += 1

    
    query = """INSERT INTO posts(title, description, content, images, category_id, data_cate) VALUES(%s, %s, %s, %s, %s, %d) WHERE NOT EXISTS (SELECT data_cate FROM posts)"""
    
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

def getDataFromDB():
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
    query = """ SELECT data_cate FROM posts """
    cur.execute(query)
    print('Row number: ', cur.rowcount)
    row = cur.fetchone()

    arrData = []
    index = 0

    while row is not None:
        # print(row)
        # row = re.sub("(", "", row)
        arrData.insert(index, row)
        index += 1
        row = cur.fetchone()
        
    
    return arrData

def checkString(string):
    ex = "toilapython"
    string = string.lower()
    ex = ex.lower()
    if string == ex:
        print('True')
    else:
        print('False')

# testStr = str("Hoài nghi về tham vọng 'Hướng Tây' của Trung Quốc")
# print(testStr)
# checkString(testStr)

# getDataFromDB()

# def findContent(data, typeFind, tagName, attr, valueAttr, getType):
#     return data.typeFind(tagName, {attr: valueAttr})getType

# def exportData(*data):
#     captions = ["Category: ", "Title: ", "Description: ", "Content: ", "URL Image: "]
#     index = 0
#     for param in data:
#         for caption in captions:
#             print(index, '.', caption, param, '\n\n')
#             index += 1