from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('172.20.0.4', 9100))
serverSocket.listen(1)

while True:
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(1024)
	print(request)
