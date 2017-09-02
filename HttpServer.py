from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 9100))
serverSocket.listen(1)

while True:
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(1024)
	print(request)
	client_connection.sendall("HTTP/1.1 200 OK")
    client_connection.close()