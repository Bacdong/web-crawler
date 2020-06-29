#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import psycopg2
import re
import django
from bs4 import BeautifulSoup

def getData(url, tagName, className):
    res = requests.get(url)

    if res.status_code == 200:
        html_detail = BeautifulSoup(res.content, "html.parser")
        result = html_detail.find(tagName, {"class": className})
        # print(result)
        
    return result

def getURLPaint(elementHTML):
    return elementHTML.find_all("a")