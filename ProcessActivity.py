
from subprocess import Popen, PIPE
import getpass
import Logger as Logger

class ProcessActivity():
    """The process class contains information about a process that can be started the Popen.
        Attibutes: 
        - processID: ID of a started process. This is not set till startProcess is called.
        - userName: username the user that started a process
        - processPath: path of the process to call
        - processArguments: any optional arguments to call with path
        - logFormat: Format for logs generated. This also sets the log destination

    """
    def __init__(self, processPath, logFormat, processArguments=""):
        self.processID = None #proccess ID does not get set till startProcess is called
        self.userName = getpass.getuser() #checks the environment variables LOGNAME, USER, LNAME and USERNAME
        self.processPath = processPath
        self.processArguments = processArguments
        self.logFormat = logFormat
        self.startProcess()

    def startProcess(self):
        """This class method starts a process and writes a log on the activity"""
        new_process = Popen([self.processPath, self.processArguments], stdout=PIPE, stderr=PIPE)
        print(new_process.communicate()) #printing process output for testing purposes
        self.processID = new_process.pid
        logger = Logger.Logger(self.logFormat, self)
        logger.writeLog()

process = ProcessActivity(processPath='pwd', processArguments="--help", logFormat="TSV")
process = ProcessActivity(processPath="./test_executables/hello_world.sh", logFormat="TSV")
process = ProcessActivity(processPath="ls", processArguments="--name", logFormat="TSV")