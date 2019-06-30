#操作mysql
# pymysql  安装： pip install pymysql
# mysql  安装：pip install mysql-connector -python
import pymysql
# from mysql import connector
from public import read_path
from public.read_conf import ReadConf

class DoMysql:
    #操作数据库的类，专门进行数据库的读取
    def do_mysql(self,query,flag=1):
        '''

        :param query: sql查询语句
        :return:
        '''
        db_config=eval(ReadConf().read_conf(read_path.config_path,'DB','db_config'))
        #第一步：连接数据库   提供数据库的连接信息
        cnn=pymysql.connect(**db_config)
        #第二步：获取游标 操作数据库的权限
        cursor=cnn.cursor()
        #第三步：操作数据库

        cursor.execute(query)
        # cursor.execute('commit') #如果是涉及到更新操作的话，我们一定要提交
        #第四步：获取查询结果，打印结果
        #每一个符合条件的数据都会存在元组里面
        if flag==1:
            res=cursor.fetchone()  #获取第一行的数据   返回元组
        else:
            res=cursor.fetchall() #获取所有的数据   返回元组嵌套元组
        return res
if __name__ == '__main__':

    query = 'select balance from `user` where id=1'
    res=DoMysql().do_mysql(query)
    print('数据库的查询结果：{}'.format(res))