from bs4 import BeautifulSoup
import re
import json

def parser(id, html):
    soup = BeautifulSoup(html, features='html.parser')

    # 右上
    try:
        face_iamge = soup.select('img.userface')[0].attrs['src']
    except:
        face_iamge = None

    try:
        city = soup.select('.user-info > a')[0].get_text()
    except:
        city = None

    try:
        registration_date = soup.select('.user-info  .pl')[0].get_text()
        registration_date = re.search(re.compile(r'[\d]{4}[-][\d]{2}[-][\d]{2}'), registration_date).group()
        introduction = soup.select('span#intro_display')[0].get_text()
    except:
        registration_date = None
        introduction = None

    # 左上
    try:
        attrs = soup.select('div.info > h1')[0]
        nickname = attrs.contents[0].strip()
        try:
            sign = attrs.contents[1].get_text()
        except:
            sign = None
    except:
        nickname = None
        sign = None

    # 右下
    try:
        broadcast_url = soup.select('div.stream-items a[target="_self"]')[0].attrs['href']
    except:
        broadcast_url = None

    try:
        concerns_num = re.search(
            re.compile(r'\d+'),
            soup.select('div#friend a[target="_self"]')[0].get_text()
        ).group()
    except:
        concerns_num = None

    try:
        follows_num = re.search(
            re.compile(r'(\d+)人关注'),
            soup.select('p.rev-link > a')[0].get_text()
        ).group(1)
    except:
        follows_num = None

    try:
        groups_num = re.search(
            re.compile(r'[(](\d+)[)]'),
            soup.select('div#group > h2')[0].get_text()
        ).group(1)
    except:
        groups_num = None

    events = {}
    try:
        events_tag = soup.select('div#event  a')
        if len(events_tag) == 0:
            raise RuntimeError('')
        events['join_num'] = re.search(
            re.compile(r'(\d+)'),
            events_tag[0].get_text()
        ).group()
        events['interested_num'] = re.search(
            re.compile(r'(\d+)'),
            events_tag[1].get_text()
        ).group()
    except:
        events['join_num'] = None
        events['interested_num'] = None

    try:
        doulist_num = re.search(
            re.compile(r'(\d+)'),
            soup.select('div#doulist  a')[0].get_text()
        ).group()
    except:
        doulist_num = None

    # 左下
    try:
        portfolio_num = re.search(
            re.compile(r'(\d+)'),
            soup.select('div#portfolio  a')[0].get_text()
        ).group()
    except:
        portfolio_num = None

    photo = {}
    try:
        photo_tag = soup.select('div#photo > h2 > span.pl > a')
        if len(photo_tag) == 0:
            raise RuntimeError('')
        photo['create_num'] = re.search(
            re.compile(r'(\d+)'),
            photo_tag[0].get_text()
        ).group()
        photo['concern_num'] = re.search(
            re.compile(r'(\d+)'),
            photo_tag[1].get_text()
        ).group()
    except:
        photo['create_num'] = None
        photo['concern_num'] = None

    book = {}
    try:
        book_tag = soup.select('div#book > h2 > span.pl > a')
        if len(book_tag) == 0:
            raise RuntimeError('')
        elif len(book_tag) == 3:
            book['reading_num'] = re.search(
                re.compile(r'(\d+)本在读'),
                book_tag[0].get_text()
            ).group(1)
            book['wanted_num'] = re.search(
                re.compile(r'(\d+)本想读'),
                book_tag[1].get_text()
            ).group(1)
            book['readed_num'] = re.search(
                re.compile(r'(\d+)本读过'),
                book_tag[2].get_text()
            ).group(1)
        elif len(book_tag) == 2:
            book['reading_num'] = None
            book['wanted_num'] = re.search(
                re.compile(r'(\d+)本想读'),
                book_tag[0].get_text()
            ).group(1)
            book['readed_num'] = re.search(
                re.compile(r'(\d+)本读过'),
                book_tag[1].get_text()
            ).group(1)
        elif len(book_tag) == 1:
            book['reading_num'] = None
            book['wanted_num'] = None
            book['readed_num'] = re.search(
                re.compile(r'(\d+)本读过'),
                book_tag[1].get_text()
            ).group(1)
    except:
        book['reading_num'] = None
        book['wanted_num'] = None
        book['readed_num'] = None

    movie = {}
    try:
        movie_tag = soup.select('div#movie > h2 > span.pl > a')
        if len(movie_tag) == 0:
            raise RuntimeError('')
        elif len(movie_tag) == 3:
            movie['watching_num'] = re.search(
                re.compile(r'(\d+)部在看'),
                movie_tag[0].get_text()
            ).group(1)
            movie['wanted_num'] = re.search(
                re.compile(r'(\d+)部想看'),
                movie_tag[1].get_text()
            ).group(1)
            movie['watched_num'] = re.search(
                re.compile(r'(\d+)部看过'),
                movie_tag[2].get_text()
            ).group(1)
        elif len(movie_tag) == 2:
            movie['reading_num'] = None
            movie['wanted_num'] = re.search(
                re.compile(r'(\d+)部想看'),
                movie_tag[0].get_text()
            ).group(1)
            movie['readed_num'] = re.search(
                re.compile(r'(\d+)部看过'),
                movie_tag[1].get_text()
            ).group(1)
        elif len(movie_tag) == 1:
            movie['reading_num'] = None
            movie['wanted_num'] = None
            movie['readed_num'] = re.search(
                re.compile(r'(\d+)部看过'),
                movie_tag[1].get_text()
            ).group(1)
    except:
        movie['watching_num'] = None
        movie['wanted_num'] = None
        movie['watched_num'] = None

    music = {}
    try:
        music_tag = soup.select('div#music > h2 > span.pl > a')
        if len(music_tag) == 0:
            raise RuntimeError('')
        elif len(music_tag) == 3:
            music['watching_num'] = re.search(
                re.compile(r'(\d+)张在听'),
                music_tag[0].get_text()
            ).group(1)
            music['wanted_num'] = re.search(
                re.compile(r'(\d+)张想听'),
                music_tag[1].get_text()
            ).group(1)
            music['watched_num'] = re.search(
                re.compile(r'(\d+)张听过'),
                music_tag[2].get_text()
            ).group(1)
        elif len(music_tag) == 2:
            music['reading_num'] = None
            music['wanted_num'] = re.search(
                re.compile(r'(\d+)张想听'),
                music_tag[0].get_text()
            ).group(1)
            music['readed_num'] = re.search(
                re.compile(r'(\d+)张听过'),
                music_tag[1].get_text()
            ).group(1)
        elif len(music_tag) == 1:
            music['reading_num'] = None
            music['wanted_num'] = None
            music['readed_num'] = re.search(
                re.compile(r'(\d+)张听过'),
                music_tag[1].get_text()
            ).group(1)
    except:
        music['watching_num'] = None
        music['wanted_num'] = None
        music['watched_num'] = None

    try:
        review_num = re.search(
            re.compile(r'\d+'),
            soup.select('div#review > h2 > span.pl > a')[0].get_text()
        ).group()
    except:
        review_num = None

    base_url = 'https://www.douban.com'
    user = {}
    user['id'] = id
    user['face_iamge'] = face_iamge
    user['city'] = city
    user['registration_date'] = registration_date
    user['introduction'] = introduction
    user['nickname'] = nickname
    user['sign'] = sign
    if broadcast_url == None:
        user['broadcast_url'] = broadcast_url
    else:
        user['broadcast_url'] = base_url + broadcast_url
    user['concerns_num'] = concerns_num
    user['follows_num'] = follows_num
    user['groups_num'] = groups_num
    user['events'] = events
    user['doulist_num'] = doulist_num
    user['portfolio_num'] = portfolio_num
    user['photo'] = photo
    user['book'] = book
    user['movie'] = movie
    user['music'] = music
    user['review_num'] = review_num

    return user

def insertJson(user, html, dao):
    json_str = json.dumps(user, ensure_ascii=False, indent=4)
    if user['broadcast_url'] == None:
        user['broadcast_url'] = 'null'
    return dao.insert(user['id'], html, json_str, user['broadcast_url'])

def updateJson(user, dao):
    json_str = json.dumps(user, ensure_ascii=False, indent=4)
    # with open('../JSON/data.json', 'w', encoding='utf-8') as json_file:
    #     json_file.write(json_str)
    if user['broadcast_url'] == None:
        user['broadcast_url'] = 'null'
    return dao.update(user['id'], json_str, user['broadcast_url'])



if __name__ == '__main__':
    f = open('../Resources/3216848.txt', 'r', encoding='utf-8')
    html = f.read()
    user = parser('123',html)
    updateJson(user)
    f = open('../JSON/data.json', 'r', encoding='utf-8')
    str = f.read()
    print(str)