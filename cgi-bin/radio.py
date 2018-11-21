#!/usr/bin/python3
import cgi,cgitb
form = cgi.FieldStorage()

if form.getvalue('site')
    site = form.getvalue(site)
else:
    site = "空数据"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title> Python3 Test </title>")
print("</head>")
print("<body>")
print("<h2>你选择的是 %s </h2>" %site)
print("</body>")
print("</html>")


