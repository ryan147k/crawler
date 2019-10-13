from Units.Mysql import DAO

dao = DAO()
user_list = dao.select()
for user in user_list:
    f = open('Douban_user/'+ user[0] + '.txt', 'w', encoding='utf-8')
    f.write(user[1])
    f.close()
