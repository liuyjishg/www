#!/usr/bin/python3
import  cgi,os
import  cgitb; cgitb.enable()

form = cgi.FieldStorage()

fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename.replace("\\","/"))
    open('/tmp/'+ fn,'wb').write(fileitem.file.read())

    message = '文件 "' + fn + '" 上传成功'

else:
    message = "文件没有上传"

print("""\
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8">
<title> Python 3 </title>
</head>
<body>
    <p>%s</p>
</body>
</html>
"""%(message))
