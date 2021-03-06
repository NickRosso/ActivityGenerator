from classes.BaseProcess import BaseProcess

class FileActivity(BaseProcess):
    """The FileActivity class is a extension of the BaseProcess class that adds a Action attribute
        Attibutes: 
        - processID: ID of a started process. This is not set till startProcess is called.
        - userName: username the user that started a process
        - command: path of the process to call
        - commandOptions: any optional arguments to call with path
        - action: Create, Delete, Update keyword to be stored in log
        - logFormat: Format for logs generated. This also sets the log destination
    """
    def __init__(self, action, command, logFormat, commandOptions=""):
        super().__init__(command, logFormat, commandOptions)
        self.action = action
        self.startProcess()

    def csv_log_format(self):
        return f"{self.processID},{self.userName},{self.processName},{self.command} {self.commandOptions},{self.commandOptions},{self.action}"

    def tsv_log_format(self):
        return f"{self.processID}\t{self.userName}\t{self.processName}\t{self.command} {self.commandOptions}\t{self.commandOptions}\t{self.action}"