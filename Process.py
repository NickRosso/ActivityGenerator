import logging as processLog
from subprocess import Popen, PIPE
import getpass

class Process():
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
        self.writeLog()

    def formatLog(self):
        """This class method sets the log format based on the log format defined in the Process"""
        if self.logFormat == 'CSV':
            processLog.basicConfig(filename="log.csv", format='%(asctime)s%(msecs)03d,%(message)s',
                level=processLog.INFO,
                datefmt='%Y-%m-%d %H:%M:%S')
            return f"{self.processID},{self.userName},{self.processPath},{self.processArguments}"

        elif self.logFormat == 'TSV':
            processLog.basicConfig(filename="log.tsv", format='%(asctime)s%(msecs)03d\t%(message)s',
                level=processLog.INFO,
                datefmt='%Y-%m-%d %H:%M:%S')
            return f"{self.processID}\t{self.userName}\t{self.processPath}\t{self.processArguments}"

    def writeLog(self):
        """This method formats the log and writes it based on the proccessLog config"""
        log_content = self.formatLog()
        processLog.info(log_content)

process = Process(processPath='pwd', processArguments="--help", logFormat="TSV")
process = Process(processPath="./test_executables/hello_world.sh", logFormat="TSV")
process = Process(processPath="ls", processArguments="--name", logFormat="TSV")