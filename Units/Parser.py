from bs4 import BeautifulSoup
import re
import json
import time

def parserBaidu(html:str, keyword:list, queue) -> bool:

    soup = BeautifulSoup(html,features='html.parser')

    news_html_list = soup.select('div#content_left div.result')
    for news_html_tag in news_html_list:
        news_html_soup = BeautifulSoup(news_html_tag.prettify(), features='html.parser')

        title_tag = news_html_soup.select('.c-title > a')[0]
        news_url = title_tag['href']
        news_title = re.sub(re.compile(r'[\s]{2,}'), '', title_tag.get_text().strip()) # 匹配连续超过两个空白符就去掉

        author_tag = news_html_soup.select('p.c-author')[0]
        author_text_list = re.sub(re.compile(r'[\s]+'), ' ', author_tag.get_text().strip()).split()
        news_author = author_text_list[0]
        news_time = author_text_list[1]
        if re.search('前', news_time):
            nowtime = time.time()
            try:
                hour = int(re.search(re.compile(r'(\d+)小时前'), news_time).group(1)[0])
            except:
                hour = 0
            try:
                minute = int(re.search(re.compile(r'(\d+)分钟前'), news_time).group(1)[0])
            except:
                minute = 0
            real_time = nowtime - hour * 60 * 60 - minute * 60
            local_time = time.localtime(real_time)
            news_time = '{}年{}月{}日 {}:{}'.format(local_time.tm_year, local_time.tm_mon, local_time.tm_mday,
                                                    local_time.tm_hour, local_time.tm_min)

        # test = news_html_soup.select('p.c-author')[0].parent
        summary_str = re.sub(re.compile(r'<p[\s\S]*?/p>'), '', news_html_soup.select('p.c-author')[0].parent.prettify())
        summary_str = re.sub(re.compile(r'<span[\s\S]*?/span>'), '', summary_str)
        news_summary = BeautifulSoup(summary_str, features='html.parser').get_text()
        news_summary = re.sub(re.compile(r'[\s]{2,}'), '', news_summary.strip())

        news_dict = {}
        news_dict['keyword'] = keyword
        news_dict['url'] = news_url
        news_dict['title'] = news_title
        news_dict['author'] = news_author
        news_dict['time'] = news_time
        news_dict['summary'] = news_summary
        json_str = json.dumps(news_dict, ensure_ascii=False)
        # with open('C:\\hurui\\project\\pycharm\\pachong-douban\\Resources\\news.jsonl', 'a', encoding='utf-8') as f:
        #     f.write(json_str + '\n')
        queue.put(json_str)

    # 判断是否有下一页
    next_page = soup.select('a.n')
    if len(next_page) == 2:
        return True
    elif len(next_page) == 1:
        a = next_page[0]
        res = re.search('下一页', next_page[0].get_text())
        return res != None
    else:
        return False



if __name__ == '__main__':
    f = open('../Resources/test.txt', 'r', encoding='utf-8')
    html = f.read()
    nextpage = parserBaidu(html, ['深圳'])
    pass