from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class ServerWorking(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>","utf-8"))
		self.wfile.write(bytes("<body><h1>Питон работает</h1>","utf-8"))
		self.wfile.write(bytes("<p> %s</p>" % self.path,"utf-8"))
		self.wfile.write(bytes("</body><html>","utf-8"))

serv_address=('',8080)
serv=HTTPServer(serv_address,ServerWorking)
serv.serve_forever()