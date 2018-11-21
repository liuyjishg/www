#!/usr/bin/python3
#coding=utf-8

import cgi,cgitb

form = cgi.FieldStorage()

site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type:text/html")
print("")
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>Test CGI </title>")
print("</head>")
print("<body>")
print("<h2>%s官网: %s</h2>"%(site_name,site_url))
print("</body>")
print("</html>")
