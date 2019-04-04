import os

#项目路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试用例路径
test_case_path=os.path.join(project_path,'testCase','test_api_1.xlsx')

# 测试报告路径
test_report_path=os.path.join(project_path,'report','test_report.html')

# 测试日志路径
test_log_path=os.path.join(project_path,'log')

#配置路径
test_conf_path=os.path.join(project_path,'config','config.conf')