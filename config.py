import json

class Global:
    __FillbackOutput = None
    __RecorderOutput = None
    __FillbackPath = None
    __RecorderPath = None
    __CommandToFillback = None
    __CommandToRecorder = None

    def __init__(self, Json):
        with open(Json, 'r') as json_file:
            config = json.load(json_file)
        self.__FillbackOutput = config["FillbackOutput"]
        self.__RecorderOutput = config["RecorderOutput"]
        self.__FillbackPath = config["FillbackPath"]
        self.__RecorderPath = config["RecorderPath"]
        self.__CommandToFillback = config["CommandToFillback"]
        self.__CommandToRecorder = config["CommandToRecorder"]

    def GetFillbackOutput(self):
        return self.__FillbackOutput

    def GetRecorderOutput(self):
        return self.__RecorderOutput

    def GetFillbackPath(self):
        return self.__FillbackPath

    def GetRecorderPath(self):
        return self.__RecorderPath

    def GetCommandToFillback(self):
        return self.__CommandToFillback

    def GetCommandToRecorder(self):
        return self.__CommandToRecorder


comm = Global("test.json")
FillbackOutputPath = comm.GetFillbackOutput()
RecorderOutputPath = comm.GetRecorderOutput()
FillbackPath = comm.GetFillbackPath()
RecorderPath = comm.GetRecorderPath()
CommandToFillback = comm.GetCommandToFillback()
CommandToRecorder = comm.GetCommandToRecorder()