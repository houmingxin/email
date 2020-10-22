# -*- coding: utf-8 -*-
# script for python3.2
import os, sys
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.encoders import encode_base64


class Mail():
    # 初始化
    def __init__(self, user, pwd, host):
        self.mail_user = user
        self.mail_pwd = pwd
        self.mail_server = smtplib.SMTP_SSL(host)
        self.mail_server.connect(host, 465)
        self.mail_server.ehlo()
        self.mail_server.login(self.mail_user, self.mail_pwd)

    def __del__(self):
        self.mail_server.close()

    # 发送邮件
    def send_mail(self, recipient, subject, text, file_path):
        msg = MIMEMultipart()
        msg["From"] = self.mail_user
        msg["Subject"] = subject
        msg["To"] = ",".join(recipient)
        msg.attach(MIMEText(text))
        msg.attach(self.get_attachment(file_path))
        self.mail_server.sendmail(self.mail_user, recipient, msg.as_string())
        print("邮件发送成功")

    # 添加邮件附件
    def get_attachment(self, file_path):
        file_name = file_path.split("\\")[-1]
        attachment = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        attachment["Content-Type"] = 'application/octet-stream'
        attachment["Content-Disposition"] = 'attachment; filename=' + file_name
        return attachment


if __name__ == '__main__':
    title = "自动化测试报告测试"
    file_path = "C:\\workhome\\test24\\pytesttest24\\result\\1b9633ae-5610-4e46-9e63-4105b2f0e833-result.json"
    with open(file_path, "r") as f:
        test_result = eval(f.readline())
    
    content = test_result["name"] + "\n" + test_result["status"]
    
    RECIPIENT = ["562182944@qq.com", "1148368634@qq.com", "2437639393@qq.com", "2457427090@qq.com"]
    mail = Mail("562182944@qq.com", "loqjgxfqgbwsbcdj", "smtp.qq.com")
    mail.send_mail(RECIPIENT, title, content, file_path)