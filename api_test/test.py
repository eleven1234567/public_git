__author__ = 'zz'
import re

# match   从头开始匹配
# str_1="www.lemfix.com"
# result=re.match("com",str_1)
# print(result)

# findall   从字符串里面找匹配的内容 是以列表返回
str_1 = "www.lemfix.com"
result = re.findall("com666", str_1)
print(result)

# search  从字符串里面寻找匹配的内容
# str_1="www.lemfix.com"
# result=re.search("com",str_1).group()
# print(result)

# 正则表达式  元字符 限定符  在线正则表达式匹配  去检查自己的表达式是否正确
# ^  $  . 匹配任意单个字符  \d 匹配任意单个数字  \w \s   元字符
# 限定符 匹配次数 + 至少匹配一次  1    ？ 至多匹配一次  0 1
#   *  任意多次   {m,n}  {3,6} 3次到6次  用的不会太多


# 字典  全局字典
Param = {"no_reg_tel": "18688773467", "member_id": '9507', "regtime": "888888"}
# 字符串
str_1 = "{'code': '10001', 'status': 1, 'data': {'regtime': '${regtime}', 'pwd': 'E10ADC3949BA59ABBE56E057F20F883E', 'regname': '小蜜蜂', 'leaveamount': '9000.00', 'mobilephone': '${no_reg_tel}', 'type': '1', 'id': ${member_id}}, 'msg': '取现成功'}"

while re.findall("\$\{(.*?)\}", str_1) != []:  # 用的就是新的字符串
    result = re.search("\$\{(.*?)\}", str_1)  # ${no_reg_tel}  ${member_id}}
    arg1 = result.group(0)  # 你所找到的匹配内容所在的字符串 ${regtime}
    print('这里是arg1:', arg1)  # ${regtime} arg1
    key = result.group(1)  # 你所匹配的内容  （.*?）匹配到的内容
    print('这里是key：', key)  # regtime
    # 字符串的替换  后面的while循环 用的是最新的str_1
    str_1 = str_1.replace(arg1, Param[key])  # 保存新的值到str_1 继续循环
    print(str_1)

# class DoRegx:
#     def do_regx(self,pattern,reg_str,global_data):
#         while re.findall(pattern,reg_str):#用的就是新的字符串
#             result=re.search(pattern,reg_str)#  ${no_reg_tel}  ${member_id}}
#             arg1=result.group(0)
#             key=result.group(1)
#             reg_str=reg_str.replace(arg1,global_data[key])#保存新的值到str_1 继续循环
#         return reg_str


# result_2=re.findall("\$\{(.*?)\}",str_1)
# print(result_2)
# while re.findall("\$\{(.*?)\}",str_1):


# regx_1="\$\{(.*?)\}"#替换内容的正则表达式
# # pattern=re.compile(regx_1)
# # print(pattern.findall(str_1))
# while pattern.findall(str_1):
#     param=pattern.search(str_1).group(0)
#     param_name=pattern.search(str_1).group(1)
#     str_1=str_1.replace(param,Param[param_name])
#     print(str_1)

# str_2='${regtime}66666'
# print(re.sub('\$\{regtime\}','5555',str_2))