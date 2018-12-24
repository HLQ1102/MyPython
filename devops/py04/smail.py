from email.mime.text import MIMEText
from smtplib import SMTP
from email.header import Header

message = MIMEText('python测试\r\n', 'plain', 'utf8')
message['From'] = Header('1102144757@qq.com', 'utf8')
message['To'] = Header('975289672@qq.com', 'utf8')
message['Subjct'] = Header('smtp test', 'utf8')

sender = '1102144757@qq.com'
receivers = ['975289672@qq.com', 'root']
smtp = SMTP('localhost')
smtp.sendmail(sender, receivers, message.as_string())

