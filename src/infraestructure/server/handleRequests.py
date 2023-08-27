from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class HandleRequests(BaseHTTPRequestHandler):
	def _set_headers(self, tipo = 'text/plain'):
		self.send_response(200)
		self.send_header('Content-type', tipo)
		self.send_header('Access-Control-Allow-Credentials', 'true')
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
		self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")
		self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
		self.end_headers()

	def _log_client(self):
		c_addr = self.client_address
		print(c_addr, self.path)

	def _get_params(self, method:str="", log:bool=False):
		params = {}
		tmpPath = self.path#http://127.0.0.1:8000/?url=video&array=1,2,3

		match method.upper():
			case "GET":
				paramsRAW:str = tmpPath.split("?")[1] #url=video%3D&array=1%2C2%2C3
				params = parse_qs(paramsRAW)#{'url': ['video='], 'array': ['1,2,3,3']}

		if log:
				print("Params:", params)

		return params

	def _set_response(self, response:int):
		if isinstance(response, bytes):#si el parametro es binario
			self.wfile.write(response)
		else:#si no se convierte a bytes
			self.wfile.write(bytes(response, 'utf-8'))
