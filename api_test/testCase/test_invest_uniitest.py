import unittest
from public.http_request import HttpRequest
from ddt import ddt,data
from public.my_log import MyLog
from public.my_excel import MyExcel
from public import path_conf
from  testCase.save_value import SaveValue
from public.do_mysql import DoMysql
import re

test_data=MyExcel(path_conf.test_case_path,'invest','init_data').my_excel()
object=SaveValue()

@ddt
class TestLoanUnittest(unittest.TestCase):
    def setUp(self):
        self.t = MyExcel(path_conf.test_case_path, 'invest', 'init_data')
        MyLog().info('--------开始执行测试用例--------')

    def tearDown(self):
        MyLog().info('执行结束')

    @staticmethod
    def do_regx(s):
        while re.search('\$\{(.*?)\}', s):
            key = re.search('\$\{(.*?)\}', s).group(0)  # 要替换的对象
            value = re.search('\$\{(.*?)\}', s).group(1)  # 根据这个可以到GetData里面拿到对应的value值，这里需要利用反射
            s = s.replace(key, str(getattr(SaveValue, value)))  # 完成替换
        return s

    @data(*test_data)
    def test_register_unittest(self,item):
        global result
        if item['param'].find('loan_id')!=-1:
            query = 'SELECT max(id) FROM loan WHERE MemberID=%s'
            query_condition = object.loan_member_id
            loan_id = DoMysql().do_mysql(query, (query_condition,), 1)[0]
            new_param = item['param'].replace('${loan_id}', str(loan_id))
            if new_param.find('${member_id}')!=-1:
                query = 'SELECT Id FROM member WHERE MobilePhone=%s'
                query_condition = object.no_reg_tel
                member_id = DoMysql().do_mysql(query, (query_condition,), 1)[0]
                new_param=new_param.replace('${member_id}',str(member_id))
        else:
            new_param = item['param']
        new_param=self.do_regx(new_param)

        res=HttpRequest().http_request(item['url'],eval(new_param),item['method'],cookies=object.COOKIES)
        if res.cookies:
            setattr(object,'COOKIES',res.cookies)
        try:
            self.assertEqual(eval(item['ExpectedResult']),res.json())
            MyLog().info('开始执行{0}条用例，用例名称:{1}'.format(item['case_id'], item['title']))
            MyLog().info('{0}用例执行成功，实际结果为：{1}'.format(item['title'], res.json()))
            result='PASS'

        except AssertionError as e:
            MyLog().info('{0}实际结果为：{1}'.format(item['title'], res.json()))
            MyLog().error('请求结果和期望结果不一致，请求结果为：{0}'.format(e))
            result='FAIL'
            raise e

        finally:
            self.t.write_data(item['case_id'] + 1, 9, str(res.json()))
            self.t.write_data(item['case_id'] + 1, 10, result)

