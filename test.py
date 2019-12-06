'''
提取豆瓣账号链接
'''
# import re
#
# with open('Resources/douban_links.txt', 'a') as f:
#     file = open('Resources/links.jsonl', 'r')
#     line = file.readline()
#     while line:
#         url = re.search(re.compile(r'http://www.douban.com/people/\d+'), line)
#         if url != None:
#             f.write(url.group() + '\n')
#         else:
#             print(line)
#         line = file.readline()

'''
连接mysql数据库
'''
# import MySQLdb
# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123456", "douban", charset='utf8' )
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()

'''
处理Mysql中的无效数据
'''
# from Units.Mysql import DAO
# from Units.Parser import parser
# import re
#
# dao = DAO()
# users = dao.select()
# f = open('Resources/available_id.txt', 'a')
# for user in users:
#     if len(re.findall(re.compile(r'review_num'),user[2])) == 0:
#         f.writelines(user[0] + '\n')
#
# available_id = open('Resources/available_id.txt', 'r').readlines()
# for i in range(len(available_id)):
#     available_id[i] = available_id[i].replace('\n', '')
# file = open('Resources/douban_links.txt', 'a')
# # with open('Resources/douban_links.txt.temp', 'r') as f:
# #     line = f.readline().replace('\n', '')
# #     while line:
# #         id = re.search(re.compile(r'\d+'), line).group()
# #         if id not in available_id:
# #             file.writelines(line + '\n')
# #         line = f.readline().replace('\n', '')
# for id in available_id:
#     file.writelines('http://www.douban.com/people/' + id + '\n')
# print(available_id)

'''
向Mysql存入Json和广播url
'''
# from Units.Mysql import DAO
# from Units.Parser import parser
# from Units.Parser import updateJson
#
# dao = DAO()
# res = dao.select()
# for item in res:
#     user = parser(item[0], item[1])
#     updateJson(user, dao)
# dao.close()

'''
测试代理是否有效
'''

'''
获取mysql中的HTML重新解析
'''
# from Units.Parser import parser
# from Units.Parser import updateJson
# from Units.Mysql import DAO
# import json
# import re
#
# f = open('Resources/available_id.txt', 'r')
# id_list = f.readlines()
# f.close()
# for i in range(len(id_list)):
#     id_list[i] = id_list[i].replace('\n', '')
# print(id_list)
#
# file = open('Resources/douban_links.txt', 'a')
# dao = DAO()
# for id in id_list:
#     html = dao.test(id)[0][0]
#     user_info = parser(id, html)
#     if user_info['nickname'] != None:
#         if updateJson(user_info, dao) == False:
#             file.writelines('http://www.douban.com/people/' + id + '\n')
#     else:
#         file.writelines('http://www.douban.com/people/' + id + '\n')

# import re
# f = open('Resources/douban_links.txt', 'r')
# ip_list = f.readlines()
# f.close()
# for i in range(len(ip_list)):
#     ip_list[i] = re.search(re.compile(r'\d+'), ip_list[i]).group()
# print(ip_list)
# print(len(ip_list))



