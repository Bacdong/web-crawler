#!/usr/bin/python3
import psycopg2

def openConnection():
    serverName = 'localhost'
    username = 'postgres'
    password = 'Faker1412'
    dbName = 'WebCrawler'

    connection = psycopg2.connect(host=serverName, database=dbName, user=username, password=password)

    try:
        cursor = connection.cursor()

        cursor.execute('SELECT version()')
        version = cursor.fetchone()
        print('Connect Successfull! \n Version: ', version)
    except:
        print('Unable to connect')
    finally:
        if connection is not None:
            connection.close()