import random

class UserAgent:
    def __init__(self):
        self.userAgent = [
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept - Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep - alive',
                # 'Cookie': 'H_PS_PSSID=; BD_HOME=0; BDSVRTM=10; BAIDUID=D6D5E41449D4CDA5A1CBBA7F148039C1:FG=1; BDRCVFR[C0p6oIjvx-c]=mk3SLVN4HKm; PSTM=1575789345; delPer=0; BIDUPSID=D6D5E41449D4CDA503F64C5FE825428E;'
            }
        ]

    def setCookie(self, cookie_list):
        res = ''
        for cookie in cookie_list:
            res = res + '{}={}; '.format(cookie['name'], cookie['value'])
        res = res.strip()
        for header in self.userAgent:
            header['Cookie'] = res

    def getHead(self):
        return self.userAgent[random.randint(0,len(self.userAgent)-1)]
