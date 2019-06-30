#接口本质   传递数据的通道  登录测试用例
#登录成功验证  手机号码为空 密码为空 未注册的手机号码登录 错误的密码
import requests
from public.my_log import MyLog
# url='http://api.nnzhp.cn/api/user/login'
# param={'username':'niuhanyang','passwd':'aA123456'}
# res=requests.post(url,param)
# print(type(res.json()))
# print(type(res.text))
# 响应数据的格式： html xml json 都可以通过text方式解析   --返回数据格式是str
# json方式解析 必须要求返回的是json格式    ---返回的是dict

class HttpRequst:
    def http_request(self,url,param,method,cookies):
        if method.upper()=='POST':
            try:
                res=requests.post(url,param,cookies=cookies)
            except AssertionError as e:
                MyLog().error('post请求报错了{}'.format(e))
        elif method.upper()=='GET':
            try:
                res=requests.get(url,param,cookies=cookies)
            except AssertionError as e:
                MyLog().error('get请求报错了{}'.format(e))
        else:
            MyLog().info('请求方法不对')

        return res.json()

if __name__ == '__main__':
    url = 'http://api.nnzhp.cn/api/user/login'
    param = {'username': 'niuhanyang', 'passwd': 'aA123456'}
    res = HttpRequst().http_request(url,param,method='post',cookies=None)
    print(res)
