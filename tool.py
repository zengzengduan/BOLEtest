import os
import re
import threading
import platform
import logging
from logging import StreamHandler
from logging import FileHandler
from config import *


def StartCommand(platform, testname):
    if platform == "WIN64":
        os.system(CommandToFillback[testname] + ">" +
                  FillbackOutputPath + "/" + testname + ".log")
    else:
        pass


def CheckLog(logfile):
    with open(logfile, 'r') as f:
        line = []
        for l in f:
            infer = re.match(r"\[E\]", l)
            if infer != None:
                line.append(l)
        return line


# fillback 测试结果记录
toppath = os.path.dirname(os.path.abspath(__file__))

fillback = logging.getLogger("fillback")
log_format = logging.Formatter('%(levelname)s: %(message)s '
                               '- %(asctime)s - ' + fillback.name)
fillback.setLevel(logging.DEBUG)
# 标准流处理器，设置的级别为WARAING
stream_handler = StreamHandler()
stream_handler.setFormatter(log_format)
stream_handler.setLevel(logging.WARNING)
fillback.addHandler(stream_handler)

# 文件处理器，设置的级别为INFO
file_handler = FileHandler(filename = toppath + '\\TESTLOG\\fillback.log', mode='w')
file_handler.setFormatter(log_format)
file_handler.setLevel(logging.INFO)
fillback.addHandler(file_handler)

# recorder 测试结果记录
toppath = os.path.dirname(os.path.abspath(__file__))

recorder = logging.getLogger("recorder")
log_format = logging.Formatter('%(levelname)s: %(message)s '
                               '- %(asctime)s - ' + recorder.name)
recorder.setLevel(logging.DEBUG)
# 标准流处理器，设置的级别为WARAING
stream_handler = StreamHandler()
stream_handler.setFormatter(log_format)
stream_handler.setLevel(logging.WARNING)
recorder.addHandler(stream_handler)

# 文件处理器，设置的级别为INFO
file_handler = FileHandler(filename = toppath + '\\TESTLOG\\recorder.log', mode='w')
file_handler.setFormatter(log_format)
file_handler.setLevel(logging.INFO)
recorder.addHandler(file_handler)

