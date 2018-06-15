import requests
import re
import time
# import http.cookiejar


class ZhiHuClient(object):
    def __init__(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        }
        self.session = requests.Session()
        # self.session.cookies = http.cookiejar.LWPCookieJar(filename='cookie')
        self.session.headers.update(headers)
        try:
            self.session.cookies.load(filename='cookie', ignore_discard=False)
        except:
            print('Cookie未能加载请登录！')

    def _get_xsrf(self):
        url = 'https://www.zhihu.com/'
        s = self.session.get(url)
        html = s.text
        xscf = re.findall('<input type="hidden" name="_xsrf" value="(.*?)"', html)[0]
        return xscf

    def _get_captcha(self):
        t = str(int(time.time() * 1000))
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=1466595391805&type=login'
        r = self.session.get(captcha_url)
        with open('captcha.jpg', 'wb') as f:
            f.write(r.content)
            f.close()

        captcha = input('open the image captcha.jpg to input captcha: ')
        return captcha

    def is_login(self):
        url = 'https://www.zhihu.com/settings/profile'
        s = self.session.get(url, allow_redirects=False)
        if s.status_code == 200:
            print('login success! ')
            return True
        else:
            return False


    def login(self, emailorphonenum, password):
        url = 'https://www.zhihu.com/'
        xsrf = self._get_xsrf()
        _headers = {
            'X-Xsrftoken': xsrf,
        }
        data = {
            '_xsrf': xsrf,
            'password': password,
            # 'captcha_type': 'cn',
        }
        email_pattern = re.compile(
            "[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?")
        if email_pattern.match(emailorphonenum):
            data['email'] = emailorphonenum
            url = url + 'login/email'
            # print(url)
        else:
            # https://www.zhihu.com/login/phone_num
            url = url + 'login/phone_num'
            data['phone_num'] = emailorphonenum
            # print(url)
        self.session.headers.update(_headers)
        login_page = self.session.post(url, data=data)
        login_code = login_page.json()
        if login_code['r'] == 1:
            print('need captcha!')
            data['captcha'] = self._get_captcha()
            self.session.post(url, data=data)
        if client.islogin():
            print('login success!')
        self.session.cookies.save()

client = ZhiHuClient()
if not client.is_login():
    client.login('18826234612', 'wuliao!123')