 #!/usr/bin/env python
  
 import socket
 TCP_IP = '127.0.0.1'
 TCP_PORT = 5005
 BUFFER_SIZE = 1024
 MESSAGE = "Hello, World!"
 
 soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 soc.connect((TCP_IP, TCP_PORT))
 soc.send(MESSAGE)
 data = soc.recv(BUFFER_SIZE)
 soc.shutdown(socket.SHUT_WR)
 soc.close()
 print ("received data:", data)
