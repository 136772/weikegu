import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendm(cont):
    try:
        sender = '136772@163.com'
        receiver = '136772@163.com'
        subject = '微客谷有卡了'
        smtpserver = 'smtp.163.com'
        username = '136772@163.com'
        password = 'zjl1367720'

        msg = MIMEText(cont)#中文需参数‘utf-8'，单字节字符不需要
        msg['Subject'] = Header(subject, 'utf-8')

        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        return '发送邮件失败'
    return '发送邮件成功'
