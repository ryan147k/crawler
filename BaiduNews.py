
from Units.Search import Search
from Units.Search import Proxy
from Units.Parser import parserBaidu
import re
import time
import requests

def get_keyword() -> list:
    with open('./Resources/keyword.txt', 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        keyword_list = []
        for line in lines:
            keyword = line.split()
            keyword_list.append(keyword)
    return keyword_list

class GetNews():
    def __init__(self):
        self.proxy = Proxy()
        self.search = Search()

    def main(self):
        url_base = 'https://www.baidu.com/s?rtt=1&tn=news&word={}&pn={}'
        keyword_list = get_keyword()
        for keyword in keyword_list:
            word = ''
            for item in keyword:
                word = word + item + '%20'
            page_num = 1
            nextpage = True
            while nextpage == True and page_num <= 30:
                url = url_base.format(word, str((page_num - 1) * 10))
                html = False
                while html == False:
                    html = self.search.getHtml(url=url, proxy=self.proxy)
                # 成功爬取
                nextpage = parserBaidu(html, keyword)
                page_num += 1
                print('{} {} url:"{}"'.format(page_num-1, self.proxy.proxy, url))


if __name__ == '__main__':
    getNews = GetNews()
    getNews.main()