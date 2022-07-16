from classes.BaseProcess import BaseProcess
import socket
import classes.Logger as Logger
import time

class NetworkActivity(BaseProcess):
    """The NetworkActivity class is a extension of the BaseProcess class that adds several attributes
        Attibutes: 
        - processID: ID of a started process. This is not set till startProcess is called.
        - userName: username the user that started a process
        - command: path of the process to call
        - commandOptions: any optional arguments to call with path
        - action: Create, Delete, Update keyword to be stored in log
        - dest_hostname: destination hostname of the socket connection
        - dest_port: destination port of the socket connection
        - src_hostname: source hostname that gets set on successful connection to hostname
        - src_port: source ip that gets set once the socket is established on client/src
        - data: byte string of data to send over socket to host
        - sentDataSize: length of byte string sent
        - receivedDataSize: length of byte string received from server. This is not set till socket response is recieved.
        - logFormat: Format for logs generated. This also sets the log destination
    """
    def __init__(self, logFormat, dest_hostname, protocol, dest_port="80", data=""):
        super().__init__(data, logFormat)
        #networkActivity specific attributes
        self.src_hostname = None
        self.src_port=None
        self.dest_hostname=dest_hostname
        self.dest_port=dest_port
        self.protocol = protocol
        self.data = str.encode(data) #encoding data to be used in socket connection
        self.sentDataSize = 0
        self.receivedDataSize = 0
        self.startNetworkActivity()

    def startNetworkActivity(self):
        # Create client socket.
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.settimeout(1)
        try:
            # Connect to dest_host over port 
            client_sock.connect((self.dest_hostname, self.dest_port))
            #getting hosts actual IP and port
            self.dest_hostname, self.dest_port = client_sock.getpeername()
            #getting clients actual IP and port
            self.src_hostname, self.src_port = client_sock.getsockname()
            # Send some data to dest
            self.sentDataSize =len(self.data)
            client_sock.sendall(self.data)
            client_sock.shutdown(socket.SHUT_WR)

            # Receive data
            chunks = []
            while True:
                data = client_sock.recv(2048)
                if not data:
                    break
                chunks.append(data)
            self.receivedDataSize= len(repr(b''.join(chunks)))
            # Disconnect from server.
            client_sock.close()
            
        except socket.timeout as e:
            print(f"Timed out connecting to {self.dest_hostname}:{self.dest_port}")

        logger = Logger.Logger(self.logFormat, self)
        logger.writeLog()

    def csv_log_format(self):
        return f"{self.processID},{self.userName},{self.processName},{self.dest_hostname},{self.dest_port} {self.src_hostname},{self.src_port},{self.sentDataSize},{self.receivedDataSize}"

    def tsv_log_format(self):
        return f"{self.processID}\t{self.userName}\t{self.processName}\t{self.dest_hostname}\t{self.dest_port} {self.src_hostname}\t{self.src_port}\t{self.sentDataSize}\t{self.receivedDataSize}"