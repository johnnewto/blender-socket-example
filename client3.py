# https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
import socket
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

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5)
server_address = ('localhost', 10000)
client.connect(server_address)
# client.send(b'CAMERA ME\n')

# After connecting, the socket should be non-blocking.
client.settimeout(0)

for i in range (500):
	time.sleep(0.1)
	try:
		message_buffer = client.recv(128)
	except BlockingIOError as ex:
		continue

	# if b'\n' not in message_buffer:
	# 	continue

	if b'\n' not in message_buffer:
		continue

	print(message_buffer)


	message, message_buffer = message_buffer.split(b'\n', 1)

	print(f'Message {message}')
	understood = handle_message(message)
	if understood:
		client.send(b'ACK\n')
	else:
		client.send(b'NOT UNDERSTOOD: ' + message + b'\n')

# time.sleep(5)
client.send(b'CLOSE\n')
time.sleep(0.1)

client.close()
