import threading
import time
from queue import Queue
import BaiduNews

def processQueue(q):
    while True:
        if q.unfinished_tasks > 0:
            news = q.get()
            with open('./Resources/news.jsonl', 'a', encoding='utf-8') as f:
                f.write(news + '\n')
    # you can delete the lines and put your code to process the queue
    #
    #        your code
    #


if __name__ == '__main__':
    q = Queue()
    getNews = BaiduNews.GetNews()
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
    t_write.start()
    for thread in threads:
        thread.join()

    time.sleep(5)
    end = time.time()
    print('total time is {}'.format(end - start))