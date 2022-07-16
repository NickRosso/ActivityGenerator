from Process import BaseProcess

class ProcessActivity(BaseProcess):
    def __init__(self, command, logFormat, commandOptions=""):
        super().__init__(command, logFormat, commandOptions)
        self.startProcess()
