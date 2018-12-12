#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import requests
if __name__ == '__man__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    print(req.text)