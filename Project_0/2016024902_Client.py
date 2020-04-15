import socket

HOST = '127.0.0.1'
PORT = 50000
BUFFER = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
sock.send('Hello, TCP Server!')

while True:
	recv = sock.recv(BUFFER)
	print('[TCP Server said] : %s' % recv)

	text = raw_input()
	sock.send(text)
	
sock.close()