#!/usr/bin/python3
import cgi,cgitb

form = cgi.FieldStorage()

if form.getvalue('textcontent'):
    text_content = form.getvalue('textcontent')
else:
    text_content = "空值"

print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>W3Cschool教程 CGI 测试实例</title>")
print ("</head>")
print ("<body>")
print ("<h2> 输入的内容是：%s</h2>" % text_content)
print ("</body>")
print ("</html>")

