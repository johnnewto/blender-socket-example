# https://pymotw.com/2/socket/tcp.html

import socket
import sys
import math
import time

message_buffer: bytes = b''

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.connect(server_address)

try:

	# Send data
	message = b'This is the message.  It will be repeated.'
	print(f'sending {message}')
	sock.sendall(message)

	# Look for the response
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print(f'received {data}')

finally:
	print('closing socket')
	sock.close()