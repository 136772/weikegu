import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendm(cont):
    try:
        sender = '136772@163.com'
        receiver = ['136772@163.com','200903124@qq.com']
        subject = '微客谷有卡了'
        smtpserver = 'smtp.163.com'
        username = '136772@163.com'
        password = 'zjl1367720'

        msg = MIMEText(cont)
        msg['Subject'] = Header(subject, 'utf-8')

        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        return '发送邮件失败',e
    return '发送邮件成功'

if __name__ == '__main__':
    print(sendm('账号: {}  \n共有物品数量:{}\n物品连接: {}\n该邮件只用于测试该爬虫提醒使用~~weikegu'))
