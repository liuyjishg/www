#!/usr/bin/python3
import cgi,cgitb

form = cgi.FieldStorage()

if form.getvalue('google')
    google_flag = "是"
else:
    google_flag = "否"

if form.getvalue('youj')
    youj_flag = "是"
else:
    youj_flag = "否"

print("Content-type:text/html")
print()
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>Python3 Test</title>")
print("</head>")
print("<body>")
print("<h2>youj 选择了: %s </h2>"%youj_flag)
print()
print("<h2>Google 选择了: %s </h2>"%google_flag)
print("</body>")
print("</html>")
print()

