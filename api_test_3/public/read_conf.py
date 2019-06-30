#配置文件 可配置
import configparser
#配置文件后缀名： conf ini  property

class ReadConf:
    def read_conf(self,conf_file,section,option):
        cf=configparser.ConfigParser()
        cf.read(conf_file,encoding='utf-8')
        value=cf.get(section,option) #section 片断    option  选项   value 值
        return value

if __name__ == '__main__':
    print(ReadConf().read_conf('config.conf','IP','ip'))