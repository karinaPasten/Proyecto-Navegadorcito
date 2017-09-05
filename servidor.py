#!/usr/bin/python
import sys, socket

print ("Inicializando Servidor con Python ...")
class Servidor:
	
	def __init__(self):
		print ("Configurando Parametros ...")
		self.host = '127.0.0.1'
		self.port = 9101
		self.www = 'documentRoot'		

	def iniciar_servidor(self):	

		print ("Iniciando servidor ...")
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		
		try:
			print("Servidor ", self.host, " : ",self.port)
			self.socket.bind(self.host, self.port)
		except Exception as e:
			try:			
				self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				self.socket.bind((self.host, self.port))
			except Exception as e:
				print("Error conexion Servidor ")
				self.apagar()
				sys.exit(1)
		self.esperando_conexiones()

	def apagar(self):

		try:
			print("Apagagado servidor ...")
			sevidor.socket.shutdown(socket.SHUT_RDWR)
		except Exception as e:
			print()				

	def esperando_conexiones(self):
		try:
			while True:
				print ("Esperando conexion ...")
				self.socket.listen(5)
				conexion, direccion = self.socket.accept()
				print("Cliente:" , direccion)

				datos_cliente = conexion.recv(1024)
				datos_string  = bytes.decode(datos_cliente)

				metodo_split = datos_string.split(' ')
				metodo = metodo_split[0]
				print( "Metodo: ",metodo)
				
				if (metodo == 'GET') | (metodo == 'HEAD'):

					request = datos_string.split(' ')					
					request = request[1]
					request = self.www + request
					
					try:
						handler = open(request,'rb')
						if (metodo == 'GET'):  
							contenido = handler.read() 
						handler.close()
						
						response = 'HTTP/1.1 200 OK '

						host = str(self.host)
						port = str(self.port)

						datos_json = '{'
						datos_json += '"path": "' + request + '", '
						datos_json += '"protocol": "HTTP/1.1", '
						datos_json += '"method": "GET", '
						datos_json += '"headers": {"Accept": "text/html", "Accept-Language": "es-ES", "Host": "' + host + ':' + port +'"}'
						datos_json += '}'

						response += 'X-RequestEcho: ' + datos_json
						response += ' Connection: close\n\n'						

						print ("Pagina encontrada (200) OK: ",request)

					except Exception as e:

						print ("Pagina no encontrada (404) : ",request)

						response = 'HTTP/1.1 404 Not Found\n'						
						response += 'Connection: close\n\n'

						contenido = "<html><body><br/><p>HTTP 404 Not Found</p></body></html>"

					response = response
					response_send =  response.encode()
					if (metodo == 'GET'):
						response_send +=  contenido

					print ("Enviado Datos: ",response_send)

					conexion.send(response_send)					
					print ("Cerrando conexion con cliente")
					conexion.close()

				else:
					print ("Metodo no encontrado")
		
		finally:
			conexion.close()
	
# Ejecutando Metodos

sevidor = Servidor()
sevidor.iniciar_servidor()