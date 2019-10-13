from Units.UserAgent import UserAgent
import requests
import time
import random

class Proxy:
    def __init__(self):
        self.proxy = self.get_proxy().content.decode('ascii').replace('b', '').replace("'", '')

    def set_proxy(self, proxy):
        self.proxy = proxy

    def get_proxy(self):
        try:
            proxy = requests.get("http://127.0.0.1:5010/get/", timeout=5)
            return proxy
        except Exception:
            print('127.0.0.1 超时重连')
            self.get_proxy()

    def delete_proxy(self):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(self.proxy))



class Search:
    def __init__(self, douban_name, douban_password):
        self.userAgent = UserAgent()
        # self.proxy = self.get_proxy().content.decode('ascii').replace('b', '').replace("'", '')
        self.session = requests.Session()
        self.headers = self.userAgent.getHead()
        self.douban_name = douban_name
        self.douban_password = douban_password

    def getHtml(self, url, proxy):
        self.headers = self.userAgent.getHead()
        retry_count = 2
        # self.proxy = self.get_proxy().content.decode('ascii').replace('b','').replace("'",'')
        while retry_count > 0:
            try:
                # 使用代理访问
                time.sleep(random.randint(3,9))
                html = self.session.get(url, headers=self.headers, timeout=3, proxies={"http": "http://{}".format(proxy.proxy)})
                return html
            except Exception:
                retry_count -= 1
        # 出错5次, 删除代理池中代理
        proxy.delete_proxy()
        proxy.proxy = proxy.get_proxy().content.decode('ascii').replace('b', '').replace("'", '')
        # print('proxy is invalid {}'.format(self.proxy))
        return False

    def getHtml2(self, url, proxy, ip):
        proxy.proxy = ip
        self.headers = self.userAgent.getHead()
        retry_count = 2
        while retry_count > 0:
            try:
                # 使用代理访问
                time.sleep(random.randint(2,8))
                html = self.session.get(url, headers=self.headers, timeout=3,
                                        proxies={"http": "http://{}".format(proxy.proxy)})
                if len(html.text) < 1000:
                    return False
                return html
            except Exception:
                retry_count -= 1
        # 出错5次, 删除代理池中代理
        return False

    # 登录
    def login(self):
        self.headers = self.userAgent.getHead()
        url = 'https://accounts.douban.com/j/mobile/login/basic'
        data = {
            'ck': '',
            'name': self.douban_name,
            'password': self.douban_password,
            'remember': 'false',
            'ticket': '',
        }
        response = self.session.post(url, headers=self.headers, data=data).json()
        if response['status'] == 'success':
            print('{} 登录成功'.format(self.douban_name))
            return True
        else:
            print('{} 登录失败'.format(self.douban_name))
            print(response)
        return False


if __name__ == '__main__':
    proxy = Proxy()
    proxy.set_proxy('113.140.1.82:53281')
    search = Search('18714890639', 'douban123456')
    # search.login()
    html = search.getHtml('http://www.douban.com', proxy)
    print(html)
