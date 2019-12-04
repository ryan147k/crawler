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
            'Cookie': 'BIDUPSID=0B51F0C45238194A1EDFBDC5AFBD68BC; PSTM=1572594501; BAIDUID=0B51F0C45238194A6AED2D00E69650FA:FG=1; BD_UPN=12314753; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; yjs_js_security_passport=194a979d11af6b68eb17d4a61aca8605f64f60fb_1575443711_js; delPer=0; BD_HOME=0; BD_CK_SAM=1; PSINO=7; H_PS_645EC=9eadTcLfOhHEwiiLjqka26%2BqArCJENNn3SN5xPmM03Fdi5XMTnBPE7ouwR8; COOKIE_SESSION=4904_0_9_8_4_1_0_0_9_1_255_0_3013_0_0_0_1575444473_0_1575456647%7C9%23325168_39_1574911494%7C9; BDRCVFR[C0p6oIjvx-c]=rJZwba6_rOCfAF9pywd; BDSVRTM=774; H_PS_PSSID='
        }
    ]
    def getHead(self):
        return self.userAgent[random.randint(0,len(self.userAgent)-1)]
