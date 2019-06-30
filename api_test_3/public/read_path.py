import os

#顶级项目路径读取出来
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试用例的存储的路径
testCase_path=os.path.join(project_path,'testCase','testCase.xlsx')

#测试报告的存储的路径
report_path=os.path.join(project_path,'report')

#日志文件的存储的路径
log_path=os.path.join(project_path,'logs')

#配置文件的存储的路径
config_path=os.path.join(project_path,'config','config.conf')