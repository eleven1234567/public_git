from public.my_excel import MyExcel
from public.http_request import HttpRequst
from public import read_path
import unittest
from testCase import test_login
from testCase import test_gold_add
import HTMLTestRunnerNew
import time
import os



#要把用例集合起来
suite=unittest.TestSuite()  #测试套件   负责搜集测试用例
loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
suite.addTest(loader.loadTestsFromModule(test_login))
suite.addTest(loader.loadTestsFromModule(test_gold_add))

now=time.strftime('%Y-%m-%d')  #获取当前时间
path='test_'+now+'.html'
new_path=os.path.join(read_path.report_path,path)
#加载测试用例？   自己去做
with open(new_path,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,title='测试测试啦',description='接口调用',tester='tester')
    runner.run(suite)


    # methodName, url, param, method, expect
    # print(type(item['case_id']))
    #
    # print('正在执行{0}条用例:{1}'.format(item['case_id'],item['title']))

# ddt