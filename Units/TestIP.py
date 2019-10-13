import requests
from Units.Search import Proxy

def loadIP():
    file = '../Resources/ip/ip_proxy.txt'
    f = open(file, 'r')
    ip_list = f.readlines()
    for i in range(len(ip_list)):
        ip_list[i] = ip_list[i].replace('\n', '')
    f.close()

    return ip_list

def testIP(ip_list):
   for IP in ip_list:
       # try:
       #     thisProxy = "http://" + IP
       #     thisIP = "".join(IP.split(":")[0:1])
       #     print(thisIP, end=' ')
       #     res = requests.get(url="http://icanhazip.com/", timeout=8, proxies={"http": thisProxy})
       #     proxyIP = res.text.replace('\n','')
       #     if (proxyIP == thisIP):
       #         print("代理IP:'" + proxyIP + "'有效！")
       #         f = open('../Resources/ip/ip_list.txt', 'a')
       #         f.writelines(IP + '\n')
       #         f.close()
       #     else:
       #         print("代理IP无效！")
       # except:
       #     print("代理IP无效！")
       try:
           thisProxy = "http://" + IP
           thisIP = "".join(IP.split(":")[0:1])
           print(thisIP, end=' ')
           res = requests.get(url="http://www.douban.com/", timeout=3, proxies={"http": thisProxy})
           if res.status_code == 200:
               print('代理IP有效' + IP)
               f = open('../Resources/ip/ip_list.txt', 'a')
               f.writelines(IP + '\n')
               f.close()
           else:
               print("代理IP无效！")
       except:
           print("代理IP无效！")

def testIP2():
    proxy = Proxy()
    while 1:
        IP = proxy.get_proxy().content.decode('ascii').replace('b', '').replace("'", '')
        proxy.set_proxy(IP)
        try:
            thisProxy = "http://" + IP
            thisIP = "".join(IP.split(":")[0:1])
            print(thisIP, end=' ')
            res = requests.get(url="http://www.douban.com", timeout=3, proxies={"http": thisProxy})
            if res.status_code == 200:
                print('代理IP有效' + IP)
                proxy.delete_proxy()
                f = open('../Resources/ip/ip_list.txt', 'a')
                f.writelines(IP + '\n')
                f.close()
            else:
                print("代理IP无效！")
                proxy.delete_proxy()
        except:
            print("代理IP无效！")
            proxy.delete_proxy()



if __name__ == '__main__':
    testIP2()
    #testIP(loadIP())
    pass