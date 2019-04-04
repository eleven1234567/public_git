import requests
from public.my_log import MyLog

class HttpRequest:
    def http_request(self,url,param,method,cookies):
        if method.upper()=='GET':
            try:
                res=requests.get(url,params=param,cookies=cookies)
            except AssertionError as e:
                MyLog().error('GET请求异常{0}'.format(e))
        elif method.upper()=='POST':
            try:
                res=requests.post(url,param,cookies=cookies)
            except AssertionError as e:
                MyLog().error('POST请求异常{0}'.format(e))
        else:
            MyLog().error('请求异常')

        return  res

if __name__ == '__main__':
    login = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    login_date = {"mobilephone": "13548773642", "pwd": "123456"}
    print(HttpRequest().http_request(login,login_date,'get',cookies=None))

