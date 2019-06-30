import unittest
from public.http_request import HttpRequst
from public.my_excel import MyExcel
from ddt import ddt,data,unpack
from public.my_log import MyLog
from public import read_path
from public import get_data
# ddt 装饰器
test_data=MyExcel(read_path.testCase_path,'test_data').my_excel()#测试数据

@ddt
class TestHttpRequest(unittest.TestCase):

    def setUp(self):#初始化  测试之前的一些准备
        self.t=MyExcel(read_path.testCase_path,'test_data')  #保存测试结果的实例
        MyLog().info('我要开始测试了')

    def tearDown(self):
        MyLog().info('我已经结束测试了')

    @data(*test_data)
    def test_http_request(self,item): #测试类里面的函数没有传参
        new_param=get_data.replace(item['param'])
        print(new_param)
        res=HttpRequst().http_request(item['url'],eval(new_param),item['method'],cookies=None)#执行http请求
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
