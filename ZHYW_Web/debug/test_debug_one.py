import os
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮件服务器
smtpserver = 'smtp.elitel.com.cn'
# 发送邮箱用户\密码
user = 'wanglishen@elitel.com.cn'
password = '243717'
# 发送邮箱
sender = 'wanglishen@elitel.com.cn'
# 接收邮箱
receiver = 'wanglishen@elitel.com.cn'
# 发送邮件主题
subject = u'邮件发送测试'
# 编写HTML邮件真跟
msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()