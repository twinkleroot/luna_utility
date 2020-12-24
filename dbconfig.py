import pymysql

class MysqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user=id, password=pw, db=db_name, charset='utf8')
        self.curs = self.conn.cursor()
    
    def select_one(self, query, param):
        self.curs.execute(query, param)
        result = self.curs.fetchone()
        self.curs.close()
        return result