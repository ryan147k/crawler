
from Units.Search import Search
from Units.Search import Proxy
from Units.Mysql import DAO
from Units.Parser import parser
from Units.Parser import insertJson
import re
import time
import requests

class Users():
    # 读取豆瓣账号和密码
    def __init__(self, douban_accounts):
        self.proxy = Proxy()
        self.searchs = []
        self.dao = DAO()
        for account in douban_accounts:
            search = Search(account['douban_name'], account['douban_password'])
            self.searchs.append(search)

        # pop = []
        # for index in range(len(self.searchs)):
        #     if self.searchs[index].login() == False:
        #         pop.append(index)
        # for i in range(len(pop)):
        #     self.searchs.pop(pop[i] - i)
        index = 0
        while self.searchs[index].login() == False:
            index += 1


    def main(self):
        f = open('Resources/douban_links.txt')
        line = f.readline()
        index = 0
        cnt = 0

        ip_list = loadIP()
        i = 0 # ip_list当前索引
        while line:
            url = line.replace('\n', '')
            id = re.search(re.compile(r'\d+'), url).group()
            # html = self.searchs[index].getHtml(url, self.proxy).text

            flag = True
            html = False

            while flag:
                try:
                    html = self.searchs[index].getHtml2(url, self.proxy, ip_list[i])
                    while (html == False):
                        print('   ' + self.proxy.proxy + ' failed!')
                        i += 1
                        # index = (index + 1) % len(self.searchs)
                        # if index == 0:
                        #     time.sleep(1)
                        html = self.searchs[index].getHtml2(url, self.proxy, ip_list[i])
                    flag = False
                except:
                    print('IP_list failed.')
                    # index = (index + 1) % len(self.searchs)
                    # if index == 0:
                    #     time.sleep(1)

                    time.sleep(10)
                    # 更新ip_list并更新索引
                    ip_list = loadIP()
                    i = 0
                    print('reload complete.')



            html = html.text

            # while html == False:
            #     html = self.searchs[index].getHtml(url, self.proxy)
            # html = html.text

            # index = (index + 1) % len(self.searchs)
            cnt += 1
            # if cnt % 300 == 0:
            #     index = (index + 1) % len(self.searchs)
            #     while self.searchs[index].login() == False:
            #         index += 1

            time.sleep(1)
            user = parser(id, html)
            print(str(cnt) + ' ' + self.proxy.proxy + ' ' + url, end='  ')

            insertJson(user, html, self.dao)
            line = f.readline()
        self.dao.close()
        

def loadAccounts():
    file = 'Resources/douban_account.txt'
    accounts = []
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.replace('\n', '').split()
        account = {}
        account['douban_name'] = line[0]
        account['douban_password'] = line[1]
        accounts.append(account)
    return accounts

def loadIP():
    file = 'Resources/ip/ip_fresh.txt'
    f = open(file, 'r')
    ip_list = f.readlines()
    f.close()
    for i in range(len(ip_list)):
        ip_list[i] = ip_list[i].replace('\n', '')

    return ip_list


if __name__ == '__main__':
    users = Users(loadAccounts())
    users.main()