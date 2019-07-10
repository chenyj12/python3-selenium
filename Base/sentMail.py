import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from configparser import ConfigParser
from Base.log import log1


# 获取最新报告
def new_file(report_dir):
    # 获取列表文件，以列表形式返回
    lists = os.listdir(report_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    # 获取最新文件的绝对路径
    file = os.path.join(report_dir, lists[-1])
    return file


# 发送邮件方法
def send_mail(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    f.close()
    # 邮件服务器内容
    config = ConfigParser()
    # 获取config配置文件地址
    file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
    config.read(file_path)
    smtpserver = 'smtp.qq.com'
    user = config.get("sender", "username")
    password = config.get("sender", "password")
    sender = config.get("sender", "email")
    receiver_list = config.get("addressed", "receivers")
    receivers = receiver_list.split(',')  # 使用split方法读取配置文件地址
    subject = '测试报告'

    # # 报告正文
    # text = "Dear all!\n附件是最新测试报告。\n麻烦下载下来观看，用户火狐浏览器打开。\n请知悉，谢谢！"
    # msg_plain = MIMEText(text, 'plain', 'utf-8')
    # msg.attach(msg_plain)

    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)
    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receivers)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receivers, msg.as_string())
    log1.info("开始发送测试报告邮件")
    smtp.quit()
    log1.info("测试报告邮件发送完成")
