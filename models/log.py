import logging
#开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件  
class Logger():
    def __init__(self, path, filename):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''
        # 创建一个logger
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:         #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler(filename)
            fh.setLevel(logging.DEBUG)

            # 再创建一个handler，用于输出到控制台
            # ch = logging.StreamHandler()
            # ch.setLevel(logging.DEBUG)

            # 定义handler的输出格式
            formatter = logging.Formatter('%(name)s - %(message)s')        # %(asctime)s - %(name)s - %(levelname)s - changed by chengjiyu on 2016/10/25
            # formatter = format_dict[int(loglevel)]
            fh.setFormatter(formatter)
            # ch.setFormatter(formatter)

            # 给logger添加handler      只需添加一次，需要移除handler，否则重复纪录日志
            self.logger.addHandler(fh)
            # self.logger.addHandler(ch)
