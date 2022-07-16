from Process import BaseProcess

class FileActivity(BaseProcess):
    def __init__(self, action, command, logFormat, commandOptions=""):
        super().__init__(command, logFormat, commandOptions)
        self.action = action
        self.startProcess()
