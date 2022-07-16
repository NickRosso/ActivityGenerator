import logging as fileActivityLog
from subprocess import Popen, PIPE
import getpass

class FileActivity():
    def __init__(self, processPath, logFormat, action):
        self.processID = None #proccess ID does not get set till startProcess is called
        self.userName = getpass.getuser() #checks the environment variables LOGNAME, USER, LNAME and USERNAME
        self.processPath = processPath
        self.action = action
        self.logFormat = logFormat
        self.performAction()


# process = FileActivity(processPath='pwd', processArguments="--help", logFormat="TSV")
# process = FileActivity(processPath="./test_executables/hello_world.sh", logFormat="TSV")
# process = FileActivity(processPath="ls", processArguments="--name", logFormat="TSV")