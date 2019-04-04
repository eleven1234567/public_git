__author__ = 'Asus'
from config.read_conf import ReadConf
from public import path_conf
import pymysql


class DoMysql:
    def __init__(self):
        self.config=eval(ReadConf().read_conf(path_conf.test_conf_path,'DB','config'))

    def do_mysql(self,query,query_condition,state):
        con=pymysql.connect(**self.config)
        cur = con.cursor()
        cur.execute(query,query_condition)
        if state==1:
            res=cur.fetchone()
        else:
            res=cur.fetchall()
        cur.close()
        con.close()
        return res

if __name__ == '__main__':
    query='SELECT LeaveAmount FROM member WHERE MobilePhone=%s'
    query_condition=('18999998369',)
    tel=DoMysql().do_mysql(query,query_condition,state=1)[0]
    print(tel)



