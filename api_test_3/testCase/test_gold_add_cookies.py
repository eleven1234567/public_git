import unittest
from public.http_request import HttpRequst
from public.my_excel import MyExcel
from ddt import ddt,data,unpack
from public.my_log import MyLog
from public import read_path
from public.get_data import GetData
# ddt 装饰器
test_data=MyExcel(read_path.testCase_path,'test_gold_add').my_excel()#测试数据

#cookies的组成：登录请求之后直接产生cookies
#充值用例
COOKIES=None  #设置这个cookies的初始值，为None
@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):#初始化  测试之前的一些准备
        self.t=MyExcel(read_path.testCase_path,'test_gold_add')  #保存测试结果的实例
        MyLog().info('我要开始测试了')

    def tearDown(self):
        MyLog().info('我已经结束测试了')

    @data(*test_data)
    def test_http_request(self,item): #测试类里面的函数没有传参
        global COOKIES #声明是一个全局变量
        res=HttpRequst().http_request(item['url'],eval(item['param']),item['method'],cookies=getattr(GetData,'COOKIES'))#执行http请求
        #每次请求之后就判断  是否产生cookies 如果生成  就替换全局变量
        #如果不产生  就不替换
        if res.cookies!={}:  # 就说请求应该是登录请求产生了cookies
            setattr(GetData,'COOKIES',res.cookies)
        
        self.t.write_data(item['case_id']+1,9,str(res)) #报存结果
        
        try:
            self.assertEqual(item['expect'],res['error_code'])  #断言的作用？  比对期望值与结果值
            test_result='PASS'
        except AssertionError as e:
            MyLog().error('执行用例的时候报错{}'.format(e))
            test_result='FAIL'
            raise e
        finally:
            self.t.write_data(item['case_id']+1,10,test_result)
