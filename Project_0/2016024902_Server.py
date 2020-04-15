import socket

def opration(number1, number2, operator):
	#calculate the result
	if operator == '+':
		number = number1 + number2
		print('value is %d' %number)
	elif operator == '-':
		number = number1 - number2
		print('value is %d' %number)
	elif operator == '*':
		number = number1 * number2
		print('value is %d' %number)
	elif operator == '/':
		number = number1 / number2
		print('value is %d' %number)

	return number


HOST = '127.0.0.1'
PORT = 50000
BUFFER = 4096

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#create the socket INET, STREAM
sock.bind((HOST, PORT))
sock.listen(0)
#wait the client

print('tcp server listen at : %s ; %s \n\r' %(HOST, PORT))

while True:
	client_sock, client_addr = sock.accept()
	print('%s:%s connected' %client_addr)

	count = 0

	while True:
		recv = client_sock.recv(BUFFER)
		#recieve the data from client

		print('[client %s %s said] : %s' %(client_addr[0], client_addr[1], recv))

		if count == 0:
			print('on first')
			client_sock.send('input 1st number  ')
			count = 1

		elif count == 1:
			print('on operator')
			client_sock.send('input operator  ')
			number1 = int(recv)
			count = 2

		elif count == 2:
			print('on second')
			client_sock.send('input 2nd number  ')
			operator = recv
			count = 3

		elif count == 3:
			 number2 = int(recv)
			 result = opration(number1, number2, operator)
			 client_sock.send('result is : %s ' %result)
			 count = 0