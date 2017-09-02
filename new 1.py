import requests
import json


def headerCreation(path, protocol, method, headers):  
  headerCall = []  
  headerCall['method'] = method
  headerCall['path'] = path
  headerCall['headers'] = json.loads(headers)
  headerCall['protocol'] = protocol 
  return headerCall
  
 @given('Servidor corriendo en localhost:9100')
def steps(context):
	requests.get("http://localhost:9100")
	
@when('El servidor solicita el camino [path], metodo [method] y el encabezado [headers]')
def steps(context, path, method, headers):
	enlace = "http://localhost:9100" + path
	req = requests.get(enlace, headers = json.loads(headers)) if method == "GET" else req = None
	req = requests.post(enlace, headers = json.loads(headers)) if method == "POST" else req = None
	req = requests.delete(enlace, headers = json.loads(headers))if method == "DELETE" else req = None
	req = requests.put(enlace, headers = json.loads(headers)) if method == "PUT" else req = None
	req = requests.head(enlace, headers = json.loads(headers)) if method == "HEAD" else req = None
	req = requests.options(enlace, headers = json.loads(headers)) if method == "OPTIONS" else req = None
	if req is None:
		ValueError('Metodo no encontrado %d' % method)

	context.result = req

@then('Respuesta de status del servidor')
def steps(r):
r = requests.get("http://localhost:9100/")
r.status_code

@then('Existencia de X_REquestEcho en el header')
def steps(context)
if "X_RequestEcho" in context.result.headers
	print 'Existe X_RequestEcho'
	

