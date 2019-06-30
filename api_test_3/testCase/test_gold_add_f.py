import unittest
from public.http_request import HttpRequst
from public.my_excel import MyExcel
from ddt import ddt,data,unpack
from public.my_log import MyLog
from public import read_path
from public.get_data import GetData
from public.do_mysql import DoMysql
from public import get_data
# ddt 装饰器
test_data=MyExcel(read_path.testCase_path,'test_gold_add').my_excel()#测试数据

#cookies的组成：cookies={'niuhanyang':sign}
#通过反射去改变cookies
#充值用例
# COOKIES=None  #设置这个cookies的初始值，为None
@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):#初始化  测试之前的一些准备
        self.t=MyExcel(read_path.testCase_path,'test_gold_add')  #保存测试结果的实例
        MyLog().info('我要开始测试了')

    def tearDown(self):
        MyLog().info('我已经结束测试了')

    @data(*test_data)
    def test_http_request(self,item): #测试类里面的函数没有传参
        # global COOKIES #声明是一个全局变量
        MyLog().info('正在执行第{}条用例'.format(item['case_id']))
        MyLog().info('执行用例的名称：{}'.format(item['title']))
        #充值前查询数据库，获取余额保存
        if item['sql'] is not None:
            sql=eval(item['sql'])['sql']
            new_sql=get_data.replace(sql)
            before_amount=DoMysql().do_mysql(new_sql)[0]  #充值前的余额

        new_param=get_data.replace(item['param'])
        res=HttpRequst().http_request(item['url'],eval(new_param),item['method'],cookies=getattr(GetData,'COOKIES'))#执行http请求
        MyLog().info('实际结果为:{}'.format(res))
        #每次请求之后就判断  是否产生sign  如果生成  就替换全局变量
        #如果不产生  就不替换
        if str(res).find('sign')!=-1:  # 就说请求应该是登录请求产生了sign
            sign=(res['login_info'])['sign']
            COOKIES={'niuhanyang':sign}
            setattr(GetData,'COOKIES',COOKIES)
        
        #充值后的判断
        # if item['sql'] is not None:
        #     after_amount=DoMysql().do_mysql(eval(item['sql'])['sql'])[0] #充值后的余额
        
        self.t.write_data(item['case_id']+1,9,str(res)) #报存结果
        
        try:
            self.assertEqual(item['expect'],res['error_code'])  #断言的作用？  比对期望值与结果值
            #再加一个断言  与的关系
            # 充值后的判断
            if item['sql'] is not None:
                sql = eval(item['sql'])['sql']
                # new_sql = get_data.replace(sql)
                new_sql='select balance from `user` where id=4'
                after_amount = DoMysql().do_mysql(new_sql)[0]  # 充值后的余额
                rechare_amount=GetData.recharge_gold #充值金额
                expect_amount=before_amount+float(rechare_amount)
                self.assertEqual(expect_amount,after_amount)  #这里有一个坑
            test_result='PASS'
        except AssertionError as e:
            MyLog().error('执行用例的时候报错{}'.format(e))
            test_result='FAIL'
            raise e
        finally:
            self.t.write_data(item['case_id']+1,10,test_result)
