#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from selenium import webdriver
# import time
# import threading

import re
from function import getData, getURLNewsLatest, checkCategory, insertDataPosts

# get latest post in page vnexpress
url = 'https://vnexpress.net/'
tagName = 'article'
className = 'item-news full-thumb article-topstory'
result = getData(url, tagName, className)
# print(result)

# get detail latest post
urlDetail = getURLNewsLatest(result)
tagNameDetail = 'div'
classNameDetail = 'sidebar-1'
mainContentDetail = getData(urlDetail, tagNameDetail, classNameDetail)
# print(mainContentDetail)

# driver = webdriver.Chrome()
# driver.get(url)
# while True:
#     time.sleep(20)
#     driver.refresh()
# driver.quit()

# dataCate = mainContentDetail.find("span", {"id": "parentCateDetail"})["data-cate"]
# dataCate = int(dataCate)
dataCate = 0;
categoryPost = mainContentDetail.find("a")["title"]
titlePost = mainContentDetail.find("h1", {"class": "title-detail"}).text
descriptionPost = mainContentDetail.find("p", {"class": "description"}).text
contentPost = mainContentDetail.find_all("p", {"class": "Normal"})

allContent = ""
for content in contentPost:
    allContent += content.text + '\n\n'

allURLImage = ""
urlImagePost = mainContentDetail.find_all("img", {"class": "lazy"})

if len(urlImagePost) > 0:
    for urlImg in urlImagePost:
        allURLImage += urlImg["data-src"] + '\n\n'
else:
    pass

# exportData(categoryPost, titlePost, descriptionPost, allContent, allURLImage)
# print('1. Category: ', categoryPost, '\n\n')
# print('2. Title: ', titlePost, '\n\n')
# print('3. Description: ', descriptionPost, '\n\n')
# print('4. Content: ', allContent, '\n\n')
# print('5. URL Image: ', allURLImage, '\n\n')

categoryId =  checkCategory(categoryPost)
# print('ID POST: ', categoryId)

# Test insert data table posts
insertDataPosts(titlePost, descriptionPost, allContent, allURLImage, categoryId, dataCate)
