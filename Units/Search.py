from Units.UserAgent import UserAgent
import requests
import time
import random
from Units.Selenium import getCookie

class Proxy:
    def __init__(self, proxy_server_address):
        self.proxy = ''
        self.proxy_pool_address = proxy_server_address

    def set_proxy(self, proxy_ip):
        self.proxy = proxy_ip

    def get_proxy_form_pool(self):
        try:
            if self.proxy == '':
                proxy = requests.get(self.proxy_pool_address + "/get", timeout=8)
                self.set_proxy(proxy.content.decode('ascii').replace('b', '').replace("'", ''))
            return self.proxy
        except Exception:
            print('proxy_pool连接超时，正在重连')
            self.get_proxy_form_pool()

    def get_proxy_from_list(self, ip_list):
        ip_list = []

    def delete_proxy(self):
        requests.get(self.proxy_pool_address + "/delete/?proxy={}".format(self.proxy))
        self.proxy = ''


class Search:
    def __init__(self, set_cookie=False):
        self.userAgent = UserAgent()
        self.session = requests.Session()
        if set_cookie:
            self.userAgent.setCookie(getCookie())
        self.headers = self.userAgent.getHead()

    def getHtml(self, url, proxy, proxy_flag=True):
        proxy.get_proxy_form_pool()
        self.headers = self.userAgent.getHead()
        retry_count = 3
        while retry_count > 0:
            try:
                # 使用代理访问
                time.sleep(1)
                if proxy_flag:
                    response = requests.get(url, headers=self.headers, timeout=3, proxies={"http": "http://{}".format(proxy.proxy)})
                else:
                    response = requests.get(url, headers=self.headers, timeout=3)
                html = response.content.decode('utf-8')
                if len(html) < 2000:
                    raise Exception('lenth < 2000!')
                return html
            except Exception:
                retry_count -= 1
        # 出错5次, 删除代理池中代理
        if proxy_flag:
            proxy.delete_proxy()
        print(proxy.proxy + ' failed')
        return False

def set(proxy):
    proxy.get_proxy_form_pool()


if __name__ == '__main__':
    test = Proxy()
    search = Search()
    html = search.getHtml('http://www.baidu.com/s?rtt=1&tn=news&word=华为%20立讯精密%20&pn=10', test)
    while 1:
        html = search.getHtml('http://www.baidu.com/s?rtt=1&tn=news&word=华为%20立讯精密%20&pn=10', test)
    print(html)