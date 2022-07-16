from subprocess import Popen, PIPE
import Logger as Logger
import psutil

class FileActivity():
    def __init__(self, command, commandOptions,logFormat, action):
        self.processID = None #proccess ID does not get set till startProcess is called
        self.userName = None #checks the environment variables LOGNAME, USER, LNAME and USERNAME
        self.processName = None
        self.command = command
        self.commandOptions = commandOptions
        self.action = action
        self.logFormat = logFormat
        self.fileAction()

    def fileAction(self):
        new_process = Popen([self.command, self.commandOptions], stdout=PIPE, stderr=PIPE)
        process = psutil.Process(new_process.pid)
        self.processID = new_process.pid
        self.processName = process.name()
        self.userName = process.username()
        logger = Logger.Logger(self.logFormat, self)
        logger.writeLog()