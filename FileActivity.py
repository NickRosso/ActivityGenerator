from subprocess import Popen, PIPE
import getpass
import Logger as Logger

class FileActivity():
    def __init__(self, processPath, processName, logFormat, action):
        self.processID = None #proccess ID does not get set till startProcess is called
        self.userName = getpass.getuser() #checks the environment variables LOGNAME, USER, LNAME and USERNAME
        self.filePath = None
        self.processName = processName
        self.processPath = processPath
        self.action = action
        self.logFormat = logFormat

        if action == "Create":
            self.createFile()

    def createFile(self):
        new_process = Popen([self.processName, self.processPath], stdout=PIPE, stderr=PIPE)
        self.processID = new_process.pid
        self.filepath = "bleh"
        logger = Logger.Logger(self.logFormat, self)
        logger.writeLog()

process = FileActivity(processPath='help.txt', processName="touch", logFormat="TSV", action="Create")
process = FileActivity(processPath="test.png", processName="touch", logFormat="TSV", action="Create")
process = FileActivity(processPath="test.csv", processName="touch", logFormat="TSV", action="Create")