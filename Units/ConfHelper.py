import json
import os

class Conf:
    current_path = os.path.dirname(__file__)

    with open(current_path + '/../Resources/crawler.conf', 'r') as f:
        conf = json.loads(f.read())
    proxy_serve_address = conf['proxy_serve_address']
    chrome_exe_path = conf['chrome_exe_path']
    chrome_driver_path = conf['chrome_driver_path']

if __name__ == '__main__':
    conf = Conf()
    pass