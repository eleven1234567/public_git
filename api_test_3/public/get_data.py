class GetData:
    #可以动态的更改、删除、获取数据
    COOKIES=None
    normal_user='niuhanyang'
    normal_pwd='aA123456'
    student_id='1'
    recharge_gold='100'



#类属性
# print(GetData.COOKIES)
# print(GetData().COOKIES)

'''
正则参数化的方法：
1、对excel里面的值进行参数化
2、在getdata里面设置属性值（参数化必须和属性名保持一致）
3、根据参数化，去获取getdata里面的属性值进行替换
'''
import re

def replace(target):
    p2='#(.*?)#'
    while re.search(p2,target):  #查找参数的字符，有就返回match object,True
        m1=re.search(p2,target) #在目标字符串里面根据正则表达式来查找，有匹配的字符串就返回对象
        key=m1.group(1)  #传参就只是返回匹配的字符串，也就是当前组的匹配字符
        value=getattr(GetData,key) #拿到我们需要去替换的值
        target=re.sub(p2,value,target,count=1)
    return target



#反射的作用：可以动态查看、增加、删除、更改类或者实例的属性
#利用反射的方法拿值
# if __name__ == '__main__':
#
#     print(getattr(GetData,'COOKIES')) #第一个参数是类名  第二个参数是属性名 getattr获取类属性的值
#     print(hasattr(GetData,'COOKIES')) #第一个参数是类名  第二个参数是属性名    hasattr判断是否有这个属性存在
#     setattr(GetData,'COOKIES',123455) #第一个参数是类名  第二个参数是属性名  #第三个参是你要设置的新值 setattr更改类属性的值
#     print(getattr(GetData,'COOKIES'))
#     print(delattr(GetData,'COOKIES')) #第一个参数是类名  第二个参数是属性名 delattr删除类的某个属性
#     print(getattr(GetData,'COOKIES'))