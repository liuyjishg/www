#!/usr/bin/python3
import multiprocessing
import time
from selenium impport webdriver
import os

url_list =['http://blog.51cto.com/passed/2321191','http://blog.51cto.com/passed/2154095']

def web(url):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get(url)
    for i in range(10000):
        try:
            driver.refresh()
            time.sleep(1)
            print('test pass: refresh successful')
        except Exception as d:
            print("Exception found",format(d))

for i in url_list*2:
    p=multiprocessing.Process(target=web,args=(i,))
    p.start()