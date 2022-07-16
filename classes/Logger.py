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
        if self.format == "CSV":
            ActivityLog.info(self.activity.csv_log_format())
        elif self.format == "TSV":
            ActivityLog.info(self.activity.tsv_log_format())