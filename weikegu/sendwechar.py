# -*- coding: utf-8 -*-


import smtplib
from email.header import Header
from email.mime.text import MIMEText


TOEMAIL = ['200903124@qq.com', '2998601175@qq.com', '13693060278@139.com', '136772@163.com', '13301157611@189.cn', '503305077@qq.com', '1835612606@qq.com']
MAILFROM = '136772@163.com'
class Mail:
    def __init__(self, mailServer="mail.server.com", user="user@mailaddress", pwd="mailpassword"):
        self.mailServer = 'smtp.163.com'
        self.user = '136772@163.com'
        self.pwd = 'zjl1367720'
        self.conn = None

    def send_mail(self,mailFrom,mailTo,msg):
        try:
            self.conn = smtplib.SMTP()
            self.conn.connect(self.mailServer)
            self.conn.login(self.user, self.pwd)
            self.conn.sendmail(mailFrom, mailTo, msg.as_string())
            self.conn.close()
            return True
        except Exception as e:
            return False

    def send_text(self, subject, text):
        msg = MIMEText(str(text))
        me = ("%s<"+MAILFROM+">") % (Header(MAILFROM, 'utf-8'),)
        msg['From'] = me
        msg['To'] = ",".join(TOEMAIL)

        # if not isinstance(subject, unicode):
        #     subject = str(subject, 'utf-8')
        msg['Subject'] = subject

        print(msg)

        return self.send_mail(me, TOEMAIL, msg)

# s = Mail()
# subject = "123123test"
# txt = '''hi,
#     testtesttestset
# '''
# # s.send_text("136772@163.com", ["136772@163.com", "200903124@qq.com"], subject, txt)
# s.send_text('测试头', '测试文本')
