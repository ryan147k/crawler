from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Units.ConfHelper import Conf

def getCookie():
    chromedrive_path = Conf.chrome_driver_path
    chrome_options = Options()
    chrome_options.binary_location = Conf.chrome_exe_path  # 这里是你指定浏览器的路径
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    try:
        print('Starting create Chrome webdriver;')
        driver = webdriver.Chrome(chromedrive_path, options=chrome_options)
    except:
        raise RuntimeError('Failed to start Chrome webdriver. Please check if the path of your chromedrive/chrome is correct. '
                           'And make sure the versions of chromedriver and chrome match.')
    print('Chrome webdriver created successfully.')
    cookie = []
    try:
        url = 'https://www.baidu.com/?tn=news'
        print('Staring catch cookie from {}'.format(url))
        driver.get(url)
        cookie = driver.get_cookies()
        print('Get cookie successfully.')
    except:
        raise RuntimeError('Failed to get cookie.')

    driver.close()
    return cookie