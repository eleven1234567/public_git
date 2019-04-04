from  testCase import test_register_unittest
from  testCase import test_recharge_unittest
from testCase import test_withdraw_unittest
from testCase import test_invest_uniitest
import unittest
import HTMLTestRunnerNew
from public import path_conf

import json
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_register_unittest))
suite.addTest(loader.loadTestsFromModule(test_recharge_unittest))
suite.addTest(loader.loadTestsFromModule(test_withdraw_unittest))
suite.addTest(loader.loadTestsFromModule(test_invest_uniitest))

with open(path_conf.test_report_path,'wb')as file:
    ruuner=HTMLTestRunnerNew.HTMLTestRunner( stream=file,title='测试',description='注册',tester='tester')
    ruuner.run(suite)
