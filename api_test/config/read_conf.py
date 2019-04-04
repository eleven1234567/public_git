import configparser

class ReadConf:
    def read_conf(self,file,section, option):
        cf=configparser.ConfigParser()
        cf.read(file)
        value=cf.get(section,option)
        return value

if __name__ == '__main__':
   print( ReadConf().read_conf('config.conf','IP','ip'))