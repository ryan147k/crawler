# import MySQLdb
#
# class DAO():
#     def __init__(self):
#         # 打开数据库连接
#         self.db = MySQLdb.connect("localhost", "root", "123456", "douban", charset='utf8' )
#         # 使用cursor()方法获取操作游标
#         self.cursor = self.db.cursor()
#
#     def close(self):
#         self.db.close()
#
#     def insert(self, id, html, json, url):
#         sql = """
#             insert into user values ('{}', '{}', '{}', '{}');
#         """.format(id, html.replace("'", "\\'").replace('"', '\\"'), json.replace("'", "\\'").replace('"', '\\"'), url)
#         try:
#             # 执行sql语句
#             self.cursor.execute(sql)
#             # 提交到数据库执行
#             self.db.commit()
#             print('insert successed')
#             return True
#         except:
#             print(json)
#             # Rollback in case there is any error
#             self.db.rollback()
#             print('insert failed')
#             return False
#
#     def update(self, id, json, url):
#         sql = """
#             update user set json = '{}',  broadcast_url = '{}' where id = '{}';
#         """.format(json.replace("'", "\\'").replace('"', '\\"'), url, id)
#         try:
#             # 执行sql语句
#             self.cursor.execute(sql)
#             # 提交到数据库执行
#             self.db.commit()
#             print('update successed')
#             return True
#         except:
#             # Rollback in case there is any error
#             self.db.rollback()
#             print('update failed')
#             return False
#
#     def select(self):
#         sql = """
#             select id, json from user;
#         """
#         try:
#             # 执行SQL语句
#             self.cursor.execute(sql)
#             # 获取所有记录列表
#             results = self.cursor.fetchall()
#             return results
#         except:
#             print ("Error: unable to fecth data")
#             return None
#
#     def test(self):
#         sql = \
#             '''delete from user where id in ('103270673', '107983042', '123974145', '130029898', '133074304', '1366149', '138068383', '139524430', '139768293', '141450367', '142047412', '144551360', '144667591', '146072848', '146556887', '146650921', '1468254', '148458302', '148478515', '148689998', '150372323', '150469739', '150949335', '151089979', '152353650', '153551011', '153663989', '153952306', '154390155', '155350458', '156220993', '156264100', '157954409', '158120729', '158242084', '158430339', '159556512', '159841065', '162646494', '163309452', '164150868', '169570389', '171655322', '172125814', '173140917', '177379137', '179733685', '180588377', '182166323', '183546163', '185485784', '188862255', '190123776', '193595586', '198253157', '2118212', '30100889', '40333164', '4569399', '52136237', '58227337', '5848679', '59535984', '60540086', '67232858', '68547528', '72372134', '73548381', '82168268', '82988329');'''.format(id)
#         print(sql)
#         try:
#             # 执行sql语句
#             self.cursor.execute(sql)
#             # 提交到数据库执行
#             self.db.commit()
#             results = self.cursor.fetchall()
#             return results
#         except:
#             # Rollback in case there is any error
#             self.db.rollback()
#             print('delete failed')
#             return False
#
#
# if __name__ == '__main__':
#     dao = DAO()
#     dao.test()
#     dao.close()
