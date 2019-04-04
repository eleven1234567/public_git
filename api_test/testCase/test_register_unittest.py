import unittest
from public.http_request import HttpRequest
from ddt import ddt,data
from public.my_log import MyLog
from public.my_excel import MyExcel
from public import path_conf
from  testCase.save_value import SaveValue

test_data=MyExcel(path_conf.test_case_path,'register','init_data').my_excel()
object=SaveValue()

@ddt
class TestRegisterUnittest(unittest.TestCase):
    def setUp(self):
        MyLog().info('--------开始执行测试用例--------')

    def tearDown(self):
        MyLog().info('执行结束')

    @data(*test_data)
    def test_register_unittest(self,item):
        global result
        url=item['url']
        param=eval(item['param'])
        method=item['method']
        expect=eval(item['ExpectedResult'])
        res=HttpRequest().http_request(url,param,method,cookies=object.COOKIES)
        if res.cookies:
            setattr(object,'COOKIES',res.cookies)
        try:
            self.assertEqual(expect,res.json())
            MyLog().info('{0}实际结果为：{1}'.format(item['title'], res.json()))
            result='PASS'

        except AssertionError as e:
            MyLog().info('{0}实际结果为：{1}'.format(item['title'], res.json()))
            MyLog().error('请求结果和期望结果不一致，请求结果为：{0}'.format(e))
            result='FAIL'
            raise e

        finally:
            MyExcel(path_conf.test_case_path, 'register', 'init_data').write_data(item['case_id'] + 1, 9, str(res.json()))
            MyExcel(path_conf.test_case_path, 'register', 'init_data').write_data(item['case_id'] + 1, 10, result)




