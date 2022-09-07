import os
import threading
from tool import *


def func_DT_fillback_file_1():
    StartCommand("WIN64", "func_DT_fillback_file_1")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_1.log")
    if len(fillbacklog) != 0:
        fillback.error("func_DT_fillback_file_1")
        for e in fillbacklog:
            fillback.error(e)
        return False
    else:
        fillback.info("pass --- func_DT_fillback_file_1")
        return True

def func_DT_fillback_file_2():
    StartCommand("WIN64", "func_DT_fillback_file_2")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_2.log")
    if len(fillbacklog) != 0:
        fillback.error("func_DT_fillback_file_2")
        for e in fillbacklog:
            fillback.error(e)
        return False
    else:
        fillback.info("pass --- func_DT_fillback_file_2")
        return True

def func_DT_fillback_file_3():
    StartCommand("WIN64", "func_DT_fillback_file_3")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_3.log")
    if len(fillbacklog) != 0:
        fillback.error("func_DT_fillback_file_3")
        for e in fillbacklog:
            fillback.error(e)
        return False
    else:
        fillback.info("pass --- func_DT_fillback_file_3")
        return True

def func_DT_fillback_file_4():
    StartCommand("WIN64", "func_DT_fillback_file_4")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_4.log")
    if len(fillbacklog) != 0:
        fillback.error("func_DT_fillback_file_4")
        for e in fillbacklog:
            fillback.error(e)
        return False
    else:
        fillback.info("pass --- func_DT_fillback_file_4")
        return True

def func_DT_fillback_file_5():
    StartCommand("WIN64", "func_DT_fillback_file_5")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_5.log")
    if len(fillbacklog) != 0:
        fillback.error("func_DT_fillback_file_5")
        for e in fillbacklog:
            fillback.error(e)
        return False
    else:
        fillback.info("pass --- func_DT_fillback_file_5")
        return True

def func_DT_fillback_file_6():
    StartCommand("WIN64", "func_DT_fillback_file_6")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_6.log")
    if len(fillbacklog) != 0:
        fillback.error("func_DT_fillback_file_6")
        for e in fillbacklog:
            fillback.error(e)
        return False
    else:
        fillback.info("pass --- func_DT_fillback_file_6")
        return True

def func_DT_fillback_file_7():
    StartCommand("WIN64", "func_DT_fillback_file_7")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_7.log")
    if len(fillbacklog) != 0:
        fillback.info("pass --- func_DT_fillback_file_7")
        return True
    else:
        return False

def func_DT_fillback_file_8():
    StartCommand("WIN64", "func_DT_fillback_file_8")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_8.log")
    if len(fillbacklog) != 0:
        fillback.error("func_DT_fillback_file_8")
        for e in fillbacklog:
            fillback.error(e)
        return False
    else:
        fillback.info("pass --- func_DT_fillback_file_8")
        return True

def func_DT_fillback_file_9():
    StartCommand("WIN64", "func_DT_fillback_file_9")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_9.log")
    if len(fillbacklog) != 0:
        fillback.error("func_DT_fillback_file_9")
        for e in fillbacklog:
            fillback.error(e)
        return False
    else:
        fillback.info("pass --- func_DT_fillback_file_9")
        return True

def func_DT_fillback_file_10():
    StartCommand("WIN64", "func_DT_fillback_file_10")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_10.log")
    if len(fillbacklog) != 0:
        fillback.info("pass --- func_DT_fillback_file_10")
        return True
    else:
        return False

def func_DT_fillback_file_11():
    StartCommand("WIN64", "func_DT_fillback_file_11")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_11.log")
    if len(fillbacklog) != 0:
        fillback.info("pass --- func_DT_fillback_file_11")
        return True
    else:
        return False

def func_DT_fillback_file_12():
    StartCommand("WIN64", "func_DT_fillback_file_12")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_12.log")
    if len(fillbacklog) != 0:
        fillback.info("pass --- func_DT_fillback_file_12")
        return True
    else:
        return False

def func_DT_fillback_file_13():
    StartCommand("WIN64", "func_DT_fillback_file_13")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_13.log")
    if len(fillbacklog) != 0:
        fillback.info("pass --- func_DT_fillback_file_13")
        return True
    else:
        return False

def func_DT_fillback_file_14():
    StartCommand("WIN64", "func_DT_fillback_file_14")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_14.log")
    if len(fillbacklog) != 0:
        fillback.info("pass --- func_DT_fillback_file_14")
        return True
    else:
        return False

def func_DT_fillback_file_16():
    StartCommand("WIN64", "func_DT_fillback_file_16")
    fillbacklog = CheckLog(FillbackOutputPath + "/func_DT_fillback_file_16.log")
    if len(fillbacklog) != 0:
        fillback.info("pass --- func_DT_fillback_file_16")
        return True
    else:
        return False