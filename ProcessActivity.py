
from subprocess import Popen, PIPE
import Logger as Logger
import psutil

class ProcessActivity():
    """The process class contains information about a process that can be started the Popen.
        Attibutes: 
        - processID: ID of a started process. This is not set till startProcess is called.
        - userName: username the user that started a process
        - command: path of the process to call
        - commandOptions: any optional arguments to call with path
        - logFormat: Format for logs generated. This also sets the log destination

    """
    def __init__(self, command, logFormat, commandOptions=""):
        self.processID = None #proccess ID does not get set till startProcess is called
        self.userName = None #checks the environment variables LOGNAME, USER, LNAME and USERNAME
        self.processName = None
        self.command = command
        self.commandOptions = commandOptions
        self.logFormat = logFormat
        self.startProcess()

    def startProcess(self):
        """This class method starts a process and writes a log on the activity"""
        new_process = Popen([self.command, self.commandOptions], stdout=PIPE, stderr=PIPE)
        self.processID = new_process.pid
        process = psutil.Process(self.processID)
        self.processName = process.name()
        self.userName = process.username()
        logger = Logger.Logger(self.logFormat, self)
        logger.writeLog()
