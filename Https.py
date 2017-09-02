import socket  
import signal  
import time    

class Server: 

 def __init__(self, port)
	 port = 9100
     self.host = ''   
     self.port = port
     self.www_dir = 'www'  

 def activate_server(self):
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try: 
		print("Iniciando servidor HTTP en", self.host, ":",self.port)
		self.socket.bind((self.host, self.port)) 
    print ("Llamada del servidor exitosa:", self.port)
	print ("Presionar Ctrl+C para apagar el servidor y salir")
	self._wait_for_connections() 

 def shutdown(self):
	try:
	print("Shutting down the server")
	s.socket.shutdown(socket.SHUT_RDWR)
	except Exception as e: