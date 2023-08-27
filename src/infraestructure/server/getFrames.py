from http.server import BaseHTTPRequestHandler, HTTPServer
import handleRequests
from os import curdir, sep
import json

import time #para usar el sleep (detener el proceso por un tiempo)
import datetime#necesario para la conversion de datetime.datetime (de la BD) a string

from urllib.parse import parse_qs

def myconverter(o):#Un convertidor, para  que el datetime.datetime pueda parsearse a JSON
    if isinstance(o, datetime.datetime):
        return o.__str__()#se retorna el datetime en formato de string

#---------------------------------------------------------------------
class GetFrames(handleRequests.HandleRequests):

	def do_GET(self):

		self._log_client()
	
		if self.path == '/':
			'''self._set_headers('text/html')
			f = open('html/index.html')
			self._set_response(f.read())
			f.close()'''
			self._set_response("hola")
		elif self.path == '/frames':
			tmpPath = self.path#http://127.0.0.1:8000/?url=video&array=1,2,3
			print("path:", tmpPath)#http://127.0.0.1:8000/?url=video%3D&array=1%2C2%2C3

			tmpPath.startswith("url")

			paramsRAW:str = tmpPath.split("?")[1]
			print("paramsRAW:", paramsRAW)#url=video%3D&array=1%2C2%2C3

			params = parse_qs(paramsRAW)
			print("params:", params)#{'url': ['video='], 'array': ['1,2,3,3']}


host = '0.0.0.0'
port = 8000
HTTPServer((host, port), GetFrames).serve_forever()
#"0.0.0.0" means it is listening on all available interfaces.
#INFO encontrado en : https://stackoverflow.com/questions/55820681/how-do-i-access-a-python-http-server-from-a-remote-connection
#MAS INFO:localhost or 127.0.0.1, you could only connect to it from the local machine, because 127.0.0.1 belongs to the loopback device. But with 0.0.0.0, the server's binding to lo, eth0 and any other network devices you might have. de : https://askubuntu.com/questions/620459/python-simplehttpserver-woking-only-with-local-machine