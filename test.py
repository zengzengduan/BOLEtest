from pydoc_data.topics import topics
import os
import re
from tool import *
import threading

def findtopic(topics):
    with open("D:/zengzeng/BOLE/datatools_2/test/fillbackoutput/func_DT_fillback_file_5.log", 'r') as f:        
        nums = []
        for topic in topics:
            num = 0
            for line in f:
                if re.search(topic, line):
                    num += 1
            nums.append(num)
        for i in range(len(topics)):
            print("topic: {}, num: {}".format(topics[i], nums[i]))

class Fillback(threading.Thread):
    __path = None
    __command = None
    __output = None

    def __init__(self, name, path, command, output):
        super().__init__(name=name)
        self.__path = path
        self. __command = command
        self.__output = output

    def run(self):
        os.chdir(FillbackPath)
        os.system(CommandToFillback[testname] + ">" +
                  FillbackOutputPath + "/" + testname + ".log")
        print("fillback is done -->> check fillbacklog")

topics = ["ADAS#0", "ADAS#1"]
findtopic(topics)
StartCommand("WIN64", "func_DT_fillback_file_16")