#!/usr/bin/python3
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@test.cn'
receivers = ['409216159@qq.com']

message = MIMEText('Python TEST mail...','plain','utf-8')
message['From'] = Header("邮件1",'utf-8')
message['To'] = Header("测试",'utf-8')

subject = 'Python SMTP test'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送")
