import requests
import json

weikeguaccount = [
    {'tmTel': '13301157612', 'tmPwd': '242628', },
    {'tmTel': '13001938805', 'tmPwd': '242628', },
    {'tmTel': '13301157614', 'tmPwd': '242628', },
    {'tmTel': '13301157615', 'tmPwd': '242628', },
    {'tmTel': '13301157616', 'tmPwd': '242628', },
]



def getcookies(weikegu):
    cookies = []
    account = ''
    loginurl = 'http://www.315wkg.com/index.php/Login/password/control//tel//gId/'

    for elem in weikegu:
        account = elem['tmTel']
        password = elem['tmPwd']
        # ha = elem['__hash__']
        postdata = {
            'tmTel': account,
            'tmPwd': password,
            # '__hash__': ha,
        }
        session = requests.Session()
        r = session.post(loginurl, data=postdata)
        jsonstr = str(r.content, 'utf-8')

        cookie = session.cookies.get_dict()
        cookies.append(cookie)
    return cookies, account


cookies, account = getcookies(weikeguaccount)
print('Get Cookies Finish!( Num:%d)' % len(cookies))
if __name__ == '__main__':
    cookies = getcookies(weikeguaccount)
    print(cookies)
