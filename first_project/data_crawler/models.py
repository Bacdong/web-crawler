#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import psycopg2
import re
import django
from bs4 import BeautifulSoup
from django.db import models

class CategoryPaint(models.Model):
    category_name = models.CharField(max_length = 40)
    
    def __str__(self):
        return self.category_name

class Paints(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    info = models.TextField()
    wrap = models.CharField(max_length = 40)
    price = models.TextField()
    info_detail = models.TextField()

    def __str__(self):
        return self.name

class SonNhaDep(models.Model):
    
    def getData(url, tagName, className):
        res = requests.get(url)

        if res.status_code == 200:
            html_detail = BeautifulSoup(res.content, "html.parser")
            result = html_detail.find(tagName, {"class": className})

        return result

    def getPaintURL(HTMLpage):
        return 
        

    