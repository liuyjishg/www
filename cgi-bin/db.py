#!/usr/bin/python3
import pymysql

db = pymysql.connect("localhost","testuser","test123","testdb")

cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()

print("Database version :%s" %data)

db.close()
