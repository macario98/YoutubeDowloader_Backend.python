from http.server import BaseHTTPRequestHandler

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

	def _set_response(self, response:int):
		if isinstance(response, bytes):#si el parametro es binario
			self.wfile.write(response)
		else:#si no se convierte a bytes
			self.wfile.write(bytes(response, 'utf-8'))
