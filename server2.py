# https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
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
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable to keep the main loop running
running = True

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print(f'starting up on {server_address[0]} port {server_address[1]}')
serv.bind(server_address)

serv.listen(5)  # 5 connections

while running:
	i = 0
	# Look at every event in the queue
	for event in pygame.event.get():
		# Did the user hit a key?
		if event.type == KEYDOWN:
			# Was it the Escape key? If so, stop the loop.
			if event.key == K_ESCAPE:
				running = False

		# Did the user click the window close button? If so, stop the loop.
		elif event.type == QUIT:
			running = False

	conn, addr = serv.accept()

	data = conn.recv(4096)
	if b'CAMERA ME' in data:
		while True:
			conn.send(f'POS {i}, {i}, {i}\n'.encode('ascii'))
			i += 1
			if i > 10:
				i = 0

			data = conn.recv(128)
			if not data: break
			print(data)

			if b'CLOSE' in data: break

	conn.close()
	print('client disconnected')
