from classes.BaseProcess import BaseProcess
import socket
import classes.Logger as Logger
import time

class NetworkActivity(BaseProcess):
    def __init__(self, logFormat, dest_hostname, protocol, dest_port="80", data=b"", src_port = "None"):
        super().__init__(data, logFormat)
        #networkActivity specific attributes
        self.src_hostname = None
        self.src_port=src_port
        self.dest_hostname=dest_hostname
        self.dest_port=dest_port
        self.protocol = protocol
        self.data = str.encode(data)
        self.sentDataSize = None
        self.receivedDataSize = None
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

            # Receive some data back.
            chunks = []
            retry_amount = 0
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
