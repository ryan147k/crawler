import random

class UserAgent:
    userAgent = [
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep - alive',
            'Cookie': 'BAIDUID=16C8941F8DBE5F2542390D16EF46DB46:FG=1; PSTM=1565681106; BIDUPSID=83B8F0D94BD2D5E304BCEA3A595F6195; BD_UPN=12314753; BDUSS=mkwdHZEU3lITEZHY0hQTVVBdzZKYnlNLU1nN0l6QTRLUWFpOUJFQ3pNQVJJZDFkRVFBQUFBJCQAAAAAAAAAAAEAAABdgM9VsL65~dXiwb3E6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABGUtV0RlLVdc; MCITY=-340%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; sugstore=0; H_PS_645EC=ed6dgdfrdGKrJQRsGXyfjDWf2FdQDOSxcoPtT6wwGukvbBZlhuX%2B6Nd755hgcrjq%2BDUq; delPer=0; BD_CK_SAM=1; PSINO=6; COOKIE_SESSION=81914_0_7_1_13_6_0_0_7_3_2_0_335408_0_6_0_1575638689_0_1575638683%7C9%2314_187_1573990777%7C9; BDRCVFR[C0p6oIjvx-c]=ddONZc2bo5mfAF9pywdpAqVuNqsus; BDSVRTM=708; H_PS_PSSID='
        }
    ]
    def getHead(self):
        return self.userAgent[random.randint(0,len(self.userAgent)-1)]
