import socket
import threading
import time
import socket
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class ThreadedServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))
		self.running = True
		self.thread = threading.Thread(target=self.listenToClient, args=())
		self.key = None

	def listen(self):
		self.sock.listen(5)
		self.thread.start()

	def listenToClient(self):
		# only one client so put listen  in here
		size = 1024
		x,y,z = 0,0,0
		while True:
			client, address = self.sock.accept()
			client.settimeout(3)
			while True:
				try:
					if self.key == K_UP:
						z += 1
					elif self.key == K_DOWN:
						z -= 1
					elif self.key == K_LEFT:
						x += 1
					elif self.key == K_RIGHT:
						x -= 1
					if self.key is not None:
						client.send(f'POS {x}, {y}, {z}\n'.encode('ascii'))
						self.key = None
						data = client.recv(size)
						if not data: break
						print(data)
						if b'CLOSE' in data: break
					else:
						time.sleep(0.01)

					if not self.running:
						return False


				except Exception as e:
					print(f'Error {e}')
					client.close()
					break
					# return False


			print('Finished Listening')

			# try:
			# 	data = client.recv(size)
			# 	# if data:
			# 	# 	# Set the response to echo back the recieved data
			# 	# 	response = data
			# 	# 	client.send(response)
			# 	# else:
			# 	# 	raise Exception('Client disconnected')
			#
			# 	if b'CAMERA ME' in data:
			# 		while True:
			# 			client.send(f'POS {i}, {i}, {i}\n'.encode('ascii'))
			# 			i += 1
			# 			if i > 10:
			# 				i = 0
			#
			# 			data = client.recv(128)
			# 			if not data: break
			# 			print(data)
			#
			# 	if b'CLOSE' in data: break
			#
			# except:
			# 	client.close()
			# 	return False

if __name__ == "__main__":
	pygame.init()

	# Define constants for the screen width and height
	SCREEN_WIDTH = 400
	SCREEN_HEIGHT = 200

	# Create the screen object
	# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	srv = ThreadedServer('localhost',10000)
	srv.listen()

	# Variable to keep the main loop running
	running = True
	while running:
		i = 0
		# Look at every event in the queue
		for event in pygame.event.get():
			# Did the user hit a key?
			if event.type == KEYDOWN:
				# Was it the Escape key? If so, stop the loop.
				if event.key == K_ESCAPE:
					running = False
				if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
					srv.key = event.key
				print(event.key)

			# Did the user click the window close button? If so, stop the loop.
			elif event.type == QUIT:
				running = False

		time.sleep(0.01)
	srv.running = False
	srv.thread.join()
	print('End')