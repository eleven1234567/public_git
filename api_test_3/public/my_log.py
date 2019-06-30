import logging
import time
from public import read_path
import os

# 日志级别：debug   info    warining   error  caritical 从左往右级别越来越严重
# 渠道
#1、日志搜集器
class MyLog:
    def my_log(self,msg,level):
        logger=logging.getLogger('collector')
        logger.setLevel('DEBUG')#包含INFO级别在内以上的日志

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')


        # 2、日志输出器
        # 控制台
        ch=logging.StreamHandler()  #渠道是指输出到控制台
        ch.setLevel('DEBUG')


        now=time.strftime('%Y-%m-%d')  #获取当前时间
        path='test_'+now+'.txt'
        new_path=os.path.join(read_path.log_path,path)
        # 指定的文件
        fh=logging.FileHandler(new_path,encoding='utf-8')
        fh.setLevel('DEBUG')

        # 3、对接
        logger.addHandler(ch)
        logger.addHandler(fh)

        ch.setFormatter(formatter)


        if level=='DEBUG':
            logger.debug(msg)
        elif level=='INFO':
            logger.info(msg)
        elif level=='WARNING':
            logger.warning(msg)
        elif level=='ERROR':
            logger.error(msg)
        elif level=='CRITICAL':
            logger.critical(msg)
            
        #添加这个  就可以解决日志重复的问题
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')


#解决日志重复的问题 ？  自己去做

if __name__ == '__main__':
    MyLog().info('不得了啦，又有同学迟到了')
    # logger.info('好好学习，天天向上~~')
    # logger.warning('小朋友今天上课了吗？')
    # logger.error('天啦噜，同学们没有听懂，完蛋啦！')
    # logger.critical('这是一个致命错误！！！请马上解决')