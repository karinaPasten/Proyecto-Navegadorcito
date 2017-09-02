from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(('172.20.0.4', 9100))
serverSocket.listen(1)

while True:
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	message = connectionSocket.recv(1024)
	print(request)
    client_connection.sendall("HTTP/1.1 200 OK")
    client_connection.close()