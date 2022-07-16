import logging as ActivityLog

class Logger:
    def __init__(self, format, activity_object):
        self.format = format
        self.activity_object = activity_object
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
        if (type(self.activity_object).__name__ == "ProcessActivity"):
            if self.format == "CSV":
                ActivityLog.info(f"{self.activity_object.processID},{self.activity_object.userName},{self.activity_object.processPath},{self.activity_object.processArguments}")
            elif self.format == "TSV":
                ActivityLog.info(f"{self.activity_object.processID}\t{self.activity_object.userName}\t{self.activity_object.processPath}\t{self.activity_object.processArguments}")
