
from Units import Search
from Units.Parser import parserBaidu
from Units.ConfHelper import Conf
import re
import time
import requests
import os

current_path = os.path.dirname(__file__)

def get_keyword() -> list:
    with open(current_path + '/./Resources/keyword.txt', 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        keyword_list = []
        for line in lines:
            keyword = line.split()
            keyword_list.append(keyword)
    return keyword_list

class GetNews():
    def __init__(self, set_cookie=False):
        proxy_serve_address = Conf.proxy_serve_address
        self.proxy = Search.Proxy(proxy_server_address=proxy_serve_address)
        self.search = Search.Search(set_cookie=set_cookie)

    def main(self, keyword, queue):
        url_base = 'https://www.baidu.com/s?rtt=1&tn=news&word={}&pn={}'
        keyword_list = get_keyword()
        page_num = 1
        nextpage = True
        word = ''
        for item in keyword:
            word = word + item + '%20'
        while nextpage == True and page_num <= 30:
            url = url_base.format(word, str((page_num - 1) * 10))
            html = False
            while html == False:
                html = self.search.getHtml(url=url, proxy=self.proxy)
            # 成功爬取
            nextpage = parserBaidu(html, keyword, queue)
            page_num += 1
            print('{} {} url:"{}"'.format(page_num-1, self.proxy.proxy, url))
