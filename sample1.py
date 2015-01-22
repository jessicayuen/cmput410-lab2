# Sample 1
import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
	print('Failed to create socket!')
	print('Error code: ' + str(msg[0]) + ', error message: ' + msg[1])
	sys.exit()

print('Socked created successfully.')