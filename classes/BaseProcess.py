
from subprocess import Popen, PIPE
import classes.Logger as Logger
import psutil
import os
from abc import ABC

class BaseProcess(ABC):
    """The BaseProcess class is a abstract base class that contains information about a process
        Attibutes: 
        - processID: ID of a started process. This is not set till startProcess is called.
        - userName: username the user that started a process
        - command: path of the process to call
        - commandOptions: any optional arguments to call with path
        - logFormat: Format for logs generated. This also sets the log destination

    """
    def __init__(self, command, logFormat, commandOptions=""):
        self.command = command
        self.commandOptions = commandOptions
        self.logFormat = logFormat
        process = psutil.Process(os.getpid())
        self.processID = os.getpid() #storing current process's pid
        self.userName = process.username() #storing current username
        self.processName = process.name()
        

    def startProcess(self):
        """This class method starts a process and writes a log on the activity"""
        new_process = Popen([self.command, self.commandOptions], stdout=PIPE, stderr=PIPE)
        self.processID = new_process.pid
        process = psutil.Process(self.processID) #overriding BaseProcess processID since we are spawning a new process
        self.processName = process.name() #overriding BaseProcess processName since we are spawning a new process
        self.userName = process.username() #overriding BaseProcess username since we are spawning a new process
        logger = Logger.Logger(self.logFormat, self)
        logger.writeLog()
