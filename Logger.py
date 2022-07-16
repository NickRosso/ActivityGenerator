import logging as ActivityLog

class Logger:
    def __init__(self, format, activity):
        self.format = format
        self.activity = activity
        self.setLoggerConfig()

    def setLoggerConfig(self):
        if self.format == "CSV":
            ActivityLog.basicConfig(filename="log.csv", format='%(asctime)s%(msecs)03d,%(message)s',
            level=ActivityLog.INFO, datefmt='%Y-%m-%d %H:%M:%S')
        elif self.format == "TSV":
            ActivityLog.basicConfig(filename="log.tsv", format='%(asctime)s%(msecs)03d\t%(message)s',
            level=ActivityLog.INFO,
            datefmt='%Y-%m-%d %H:%M:%S')
        else:
            ActivityLog.basicConfig(filename="log.csv", format='%(asctime)s%(msecs)03d,%(message)s',
            level=ActivityLog.INFO, datefmt='%Y-%m-%d %H:%M:%S')

    def writeLog(self):
        if (type(self.activity).__name__ == "ProcessActivity"):
            if self.format == "CSV":
                ActivityLog.info(f"{self.activity.processID},{self.activity.userName},{self.activity.command},{self.activity.commandOptions}")
            elif self.format == "TSV":
                ActivityLog.info(f"{self.activity.processID}\t{self.activity.userName}\t{self.activity.command}\t{self.activity.commandOptions}")
        
        elif (type(self.activity).__name__ == "FileActivity"):
            if self.format == "CSV":
                ActivityLog.info(f"{self.activity.processID},{self.activity.userName},{self.activity.processName},{self.activity.command} {self.activity.commandOptions},{self.activity.commandOptions},{self.activity.action}")
            elif self.format == "TSV":
                ActivityLog.info(f"{self.activity.processID}\t{self.activity.userName}\t{self.activity.processName}\t{self.activity.command} {self.activity.commandOptions}\t{self.activity.commandOptions}\t{self.activity.action}")
