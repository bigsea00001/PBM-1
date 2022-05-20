import logging.handlers
import os


class CustomLogger:
    def __init__(self):
        self.logger = self.config()

    def config(self, log_name='CustomLogger', log_dir='Data/log/CustomLogger.log'):
        logger = logging.getLogger(log_name)
        formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s \
                                     > %(message)s')

        fileHandler = logging.FileHandler(log_dir)
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        logger.addHandler(fileHandler)
        logger.addHandler(streamHandler)
        logger.setLevel(logging.DEBUG)
        return logger
