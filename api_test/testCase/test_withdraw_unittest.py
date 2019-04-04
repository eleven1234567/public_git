import unittest
from public.http_request import HttpRequest
from ddt import ddt,data
from public.my_log import MyLog
from public.my_excel import MyExcel
from public import path_conf
from  testCase.save_value import SaveValue
from public.do_mysql import DoMysql
import re


test_data=MyExcel(path_conf.test_case_path,'withdraw','init_data').my_excel()

object=SaveValue()

@ddt
class TestWithdrawUnittest(unittest.TestCase):
    def setUp(self):
        self.t=MyExcel(path_conf.test_case_path,'withdraw','init_data')
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
        # global before_amount
        global  sql_result
        # global after_amount
        new_param=eval(self.do_regx(item['param']))
        if item['CheckSql']!=None:
            new_checksql=eval(self.do_regx(item['CheckSql']))
            query=new_checksql['query']
            query_condition=new_checksql['query_condition']
            # 提现前的金额
            before_amount=DoMysql().do_mysql(query,query_condition,state=1)[0]


        res=HttpRequest().http_request(item['url'],new_param,item['method'],cookies=object.COOKIES)

        if res.cookies:
            setattr(object,'COOKIES',res.cookies)

        if item['CheckSql'] != None:
            new_checksql = eval(self.do_regx(item['CheckSql']))
            query = new_checksql['query']
            query_condition = new_checksql['query_condition']
            # 提现后的金额
            after_amount = DoMysql().do_mysql(query, query_condition, state=1)[0]
            withdrawAmount=int(float(before_amount)-float(after_amount))   #提现金额

            try:
                self.assertEqual(object.draw_amount,withdrawAmount)
                MyLog().info('提现成功')
                sql_result = 'PASS'

            except AssertionError as e:
                MyLog().error('请求结果和期望结果不一致，请求结果为：{0}'.format(e))
                sql_result = 'FAIL'
                raise e

            finally:
                MyLog().info('数据库查询出的充值金额为：{}'.format(int(float(before_amount)-float(after_amount))))
                self.t.write_data(item['case_id'] + 1, 11, sql_result)

        if item['ExpectedResult'].find('${leaveamount}')>-1:
            new_ExpectedResult=item['ExpectedResult'].replace('${leaveamount}',str(after_amount))
            if new_ExpectedResult.find('member_id')>-1:
                query='SELECT id FROM member WHERE MobilePhone=%s'
                query_condition=(new_param['mobilephone'],)
                member_id=DoMysql().do_mysql(query,query_condition,state=1)[0]
                new_ExpectedResult=new_ExpectedResult.replace('${member_id}',str(member_id))
                if new_ExpectedResult.find('${regtime}')>-1:
                    query = 'SELECT RegTime FROM member WHERE MobilePhone=%s'
                    query_condition = (new_param['mobilephone'],)
                    regtime=str(DoMysql().do_mysql(query,query_condition,state=1)[0])+'.0'
                    new_ExpectedResult=new_ExpectedResult.replace('${regtime}',regtime)
                    if new_ExpectedResult.find('${no_reg_tel}')>-1:
                        new_ExpectedResult=self.do_regx(new_ExpectedResult)

        else:
            new_ExpectedResult = item['ExpectedResult']



        try:
            self.assertEqual(eval(new_ExpectedResult), res.json())
            MyLog().info('{0}实际结果为：{1}'.format(item['title'], res.json()))
            self.t.write_data(item['case_id'] + 1, 10, 'PASS')

        except AssertionError as e:
            MyLog().info('{0}实际结果为：{1}'.format(item['title'], res.json()))
            MyLog().error('请求结果和期望结果不一致，请求结果为：{0}'.format(e))
            self.t.write_data(item['case_id'] + 1, 10, 'FAIL')
            raise e
        finally:
            self.t.write_data(item['case_id'] + 1, 9, str(res.json()))





