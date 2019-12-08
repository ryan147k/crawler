import threading
import time
from queue import Queue
import BaiduNews
import os

current_path = os.path.dirname(__file__)

def processQueue(q):
    while True:
        if q.unfinished_tasks > 0:
            news = q.get()
            with open(current_path + '/./Resources/news.jsonl', 'a', encoding='utf-8') as f:
                f.write(news + '\n')
    # you can delete the lines and put your code to process the queue
    #
    #        your code
    #


if __name__ == '__main__':
    q = Queue()
    # if you want to set cookie, add the argument set_cookie=True.
    getNews = BaiduNews.GetNews(set_cookie=True)
    # put your keyword in Resources/keyword.txt
    keyword_list = BaiduNews.get_keyword()

    start = time.time()

    # create a thread for each keyword
    threads = []
    for keyword in keyword_list:
        t = threading.Thread(target=getNews.main, args=(keyword, q, ))
        threads.append(t)
        t.start()
    # create a thread for get news from the queue, and then write into the jsonl file
    t_write = threading.Thread(target=processQueue, args=(q, ))
    # when father thread finished, son threads whose daemon equal Ture will be finished compulsorily
    t_write.daemon = True
    t_write.start()
    for thread in threads:
        thread.join()

    time.sleep(5)
    end = time.time()
    print('total time is {}'.format(end - start))