# import to use Server
import BaseHTTPServer 
from SocketServer import ThreadingMixIn
host = '0.0.0.0'

# Response handler
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	# action for request 'get'
	def do_GET(self):
		print self.path
		# First connect(/) or connect to '/index.html'
		if (self.path.endswith('/index.html')):
			self.protocol_version = 'HTTP/1.1'
			# Connect to 'index.html' in directory
			f = open('./index.html')
			# Add log
			print('test1')
			# Response(200) means you got request well
			self.send_response(200)
			# Add header
			self.send_header('Content-Type', 'text/html')
			print('test2')
			#self.send_header('content-length', 500000)
			self.end_headers()
			# Setting text that set on the server
			self.wfile.write(f.read())
			f. close()
			return

		# connect to '/image.jpg'
		elif self.path.endswith('/image.jpg'):
			self.protocol_version = 'HTTP/1.1'
			f = open('./image.jpg')
			self.send_response(200)
			print('testImage')
			self.send_header('Content-Type', 'image/jpg')
			#self.send_header('Content-length', 500000)
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
			return


		# HTTP/1.0
		elif self.request_version == 'HTTP/1.0':
			# 400 error
			self.send_error(400, 'BAD REQUEST')
			print('test400')
			self.wfile.write(f.read())


		# Connect another path or exception
		else:
			# 404 error
			self.send_error(404, 'NOT FOUND')
			print('test404')
			self.wfile.write(f.read())


	# action for request 'put'
	def do_PUT(self):
		print('===== PUT =====')
		print(self.headers)
		length = int(self.headers['content-length'])
		content = self.rfile.read(length)
		# Response(200) means you got request well
		self.send_response(200)
		print(content)

	# action for request 'post'
	def do_POST(self):
		print('\n===== Request Start =====\n')
		request_path = self.path
		print(request_path)

		request_headers = self.headers
		content_length = request_headers.getheaders('content_length')
		length = int(content_length[0]) if content_length else 0

		print(request_headers)
		print(self, rfile.read(length))
		print('\n===== Request End =====\n')

		# Response(200) means you got request well
		self.send_response(200)

# Inherit ThreadHTTPServer to handle requests in a separate thread.
class ThreadHTTPServer(ThreadingMixIn, BaseHTTPServer.HTTPServer):
	pass

# Main part
if __name__ == '__main__':
	# Declare Server -> host & port with the class server 'MyHandler'
	server = BaseHTTPServer.HTTPServer(('', 9090), MyHandler)
	print('Started WebServer on port 9090')
	print('Press Ctrl + C to quit webserver')
	# makes work server
	server.serve_forever()



