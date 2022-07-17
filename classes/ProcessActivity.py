from classes.BaseProcess import BaseProcess

class ProcessActivity(BaseProcess):
    def __init__(self, command, logFormat, commandOptions=""):
        super().__init__(command, logFormat, commandOptions)
        self.startProcess()

    def csv_log_format(self):
        return f"{self.processID},{self.userName},{self.command},{self.commandOptions}"

    def tsv_log_format(self):
        return f"{self.processID}\t{self.userName}\t{self.command}\t{self.commandOptions}"
