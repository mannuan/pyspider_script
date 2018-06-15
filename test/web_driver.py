"""
selenium web driver for js fetcher
"""

import urlparse
import json
import time
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def handle_post():
    if request.method == 'GET':
        body = "method not allowed!"
        headers = {
            'Cache': 'no-cache',
            'Content-Length': len(body)
        }
        return body, 403, headers
    else:
        start_time = datetime.datetime.now()
        raw_data = request.get_data()
        fetch = json.loads(raw_data, encoding='utf-8')
        print('fetch=', fetch)

        result = {'orig_url': fetch['url'],
                  'status_code': 200,
                  'error': '',
                  'content': '',
                  'headers': {},
                  'url': '',
                  'cookies': {},
                  'time': 0,
                  'js_script_result': '',
                  'save': '' if fetch.get('save') is None else fetch.get('save')
                  }

        driver = InitWebDriver.get_web_driver(fetch)
        try:
            InitWebDriver.init_extra(fetch)

            driver.get(fetch['url'])

            # first time will sleep 2 seconds
            if InitWebDriver.isFirst:
                time.sleep(2)
                InitWebDriver.isFirst = False

            result['url'] = driver.current_url
            result['content'] = driver.page_source
            result['cookies'] = _parse_cookie(driver.get_cookies())
        except Exception as e:
            result['error'] = str(e)
            result['status_code'] = 599

        end_time = datetime.datetime.now()
        result['time'] = (end_time - start_time).seconds

        # print('result=', result)
        return json.dumps(result), 200, {
            'Cache': 'no-cache',
            'Content-Type': 'application/json',
        }


def _parse_cookie(cookie_list):
    if cookie_list:
        cookie_dict = dict()
        for item in cookie_list:
            cookie_dict[item['name']] = item['value']
        return cookie_dict
    return {}


class InitWebDriver(object):
    _web_driver = None
    isFirst = True

    @staticmethod
    def _init_web_driver(fetch):
        if InitWebDriver._web_driver is None:
            options = Options()
            # set proxy
            if fetch.get('proxy'):
                if '://' not in fetch['proxy']:
                    fetch['proxy'] = 'http://' + fetch['proxy']
                proxy = urlparse.urlparse(fetch['proxy']).netloc
                options.add_argument('--proxy-server=%s' % proxy)

            # reset headers, for now, do nothing
            set_header = fetch.get('headers') is not None
            if set_header:
                fetch['headers']['Accept-Encoding'] = None
                fetch['headers']['Connection'] = None
                fetch['headers']['Content-Length'] = None

            if set_header and fetch['headers']['User-Agent']:
                options.add_argument('user-agent=%s' % fetch['headers']['User-Agent'])

            # disable load images
            if fetch.get('load_images'):
                options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

            # set viewport
            fetch_width = fetch.get('js_viewport_width')
            fetch_height = fetch.get('js_viewport_height')
            width = 1024 if fetch_width is None else fetch_width
            height = 768 * 3 if fetch_height is None else fetch_height
            options.add_argument('--window-size={width},{height}'.format(width=width, height=height))

            # headless mode
            options.add_argument('--headless')

            InitWebDriver._web_driver = webdriver.Chrome(chrome_options=options, port=10001)

    @staticmethod
    def get_web_driver(fetch):
        if InitWebDriver._web_driver is None:
            InitWebDriver._init_web_driver(fetch)
        return InitWebDriver._web_driver

    @staticmethod
    def init_extra(fetch):
        # maybe throw TimeOutException
        driver = InitWebDriver._web_driver
        if fetch.get('timeout'):
            driver.set_page_load_timeout(fetch.get('timeout'))
            driver.set_script_timeout(fetch.get('timeout'))
        else:
            driver.set_page_load_timeout(20)
            driver.set_script_timeout(20)

            # # reset cookie
            # cookie_str = fetch['headers']['Cookie']
            # if fetch.get('headers') and cookie_str:
            #     # driver.delete_all_cookies()
            #     cookie_dict = dict()
            #     for item in cookie_str.split('; '):
            #         key = item.split('=')[0]
            #         value = item.split('=')[1]
            #         cookie_dict[key] = value
            #     # driver.add_cookie(cookie_dict)

    @staticmethod
    def quit_web_driver():
        if InitWebDriver._web_driver is not None:
            InitWebDriver._web_driver.quit()


if __name__ == '__main__':
    app.run('0.0.0.0', 9000)
    InitWebDriver.quit_web_driver()