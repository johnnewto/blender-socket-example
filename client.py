# https://pymotw.com/2/socket/tcp.html

import socket
import sys
import math
import time

def handle_message(message: bytes) -> bool:
	if message.startswith(b'POS'):
		coords = [float(part) for part in message[4:].split(b',')]
		# context.scene.camera.location = coords
		return True

	if message.startswith(b'ROT'):
		eulers_deg = (float(part) for part in message[4:].split(b','))
		eulers_rad = [math.radians(angle) for angle in eulers_deg]
		# context.scene.camera.rotation_euler = eulers_rad
		return True

	if message.startswith(b'FRAME'):
		frame_nr = int(message[6:])
		# context.scene.frame_set(frame_nr)
		return True

	return False

message_buffer: bytes = b''

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')
sock.connect(server_address)

while True:
	time.sleep(0.01)
	try:

		# Send data
		message = b'This is the message.  It will be repeated.'
		print (f'sending {message}')
		sock.sendall(message)

		# Look for the response
		amount_received = 0
		amount_expected = len(message)

		while amount_received < amount_expected:
			data = sock.recv(8)
			amount_received += len(data)
			print(f'received {data}')
		try:
			message_buffer += sock.recv(128)
		except BlockingIOError as ex:
			continue

		if b'\n' not in message_buffer:
			continue

		message, message_buffer = message_buffer.split(b'\n', 1)

		understood = handle_message(message)
		if understood:
			sock.send(b'ACK\n')
		else:
			sock.send(b'NOT UNDERSTOOD: ' + message + b'\n')
	finally:
		print('closing socket')
		sock.close()

print('closing socket')
sock.close()