import logging as processLog
from subprocess import Popen, PIPE


class Process():

    def __init__(self, userName, processName, processCLIArgs, logFormat):
        self.processID = None #proccess ID does not get set till startProcess is called
        self.userName = userName
        self.processName = processName
        self.processCLIArgs = processCLIArgs
        self.logFormat = logFormat
        self.startProcess()

    def startProcess(self):
        new_process = Popen(['python3', self.processName], stdout=PIPE, stderr=PIPE)
        self.processID = new_process.pid
        self.writeLog(self.logFormat)

    def writeLog(self, format):
        if format == 'CSV':
            processLog.basicConfig(filename="log.csv", format='%(asctime)s%(msecs)03d,%(message)s',
                level=processLog.INFO,
                datefmt='%Y-%m-%d %H:%M:%S')
            processLog.info(f"{self.processID},{self.userName},{self.processName},{self.processCLIArgs}")
        elif format == 'TSV':
            processLog.basicConfig(filename="log.tsv", format='%(asctime)s%(msecs)03d\t%(message)s',
                level=processLog.INFO,
                datefmt='%Y-%m-%d %H:%M:%S')
            processLog.info(f"{self.processID}\t{self.userName}\t{self.processName}\t{self.processCLIArgs}")

process = Process(userName="Nick", processName="./hello_world.py", processCLIArgs="-n name", logFormat="CSV")