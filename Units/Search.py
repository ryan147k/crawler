from Units.UserAgent import UserAgent
import requests
import time
import random

proxy_pool_address = 'http://112.124.25.99:8090'

class Proxy:
    def __init__(self):
        self.proxy = None

    def set_proxy(self, proxy_ip):
        self.proxy = proxy_ip

    def get_proxy_form_pool(self):
        try:
            proxy = requests.get(proxy_pool_address + "/get", timeout=5)
            return proxy
        except Exception:
            print('127.0.0.1 超时重连')
            self.get_proxy_form_pool()

    def get_proxy_from_list(self, ip_list):
        ip_list = []

    def delete_proxy(self):
        requests.get(proxy_pool_address + "/delete/?proxy={}".format(self.proxy))



class Search:
    def __init__(self):
        self.userAgent = UserAgent()
        self.session = requests.Session()
        self.headers = self.userAgent.getHead()

    def getHtml(self, url, proxy, proxy_flag=True):
        proxy.get_proxy_form_pool().content.decode('ascii').replace('b', '').replace("'", '')
        self.headers = self.userAgent.getHead()
        retry_count = 2
        while retry_count > 0:
            try:
                # 使用代理访问
                time.sleep(1)
                if proxy_flag:
                    html = self.session.get(url, headers=self.headers, timeout=3, proxies={"http": "http://{}".format(proxy.proxy)})
                else:
                    html = self.session.get(url, headers=self.headers, timeout=3)
                return html
            except Exception:
                retry_count -= 1
        # 出错5次, 删除代理池中代理
        if proxy_flag:
            proxy.delete_proxy()
        return False


if __name__ == '__main__':
    proxy = Proxy()
    proxy.get_proxy_form_pool()
    search = Search()
    html = search.getHtml('https://www.baidu.com/s?rtt=1&tn=news&word=深圳&pn=10', proxy)
    print(html)
