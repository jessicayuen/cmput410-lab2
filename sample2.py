# Sample 2
import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
	print('Failed to create socket!')
	print('Error code: ' + str(msg[0]) + ', error message: ' + msg[1])
	sys.exit()

print('Socked created successfully.')

host = 'www.ualberta.ca'
port = 80

try:
	remote_ip = socket.gethostbyname(host)
except socket.gaierror: # short for get address info error, i.e. bad url
	print('Host name could not be resolved.')
	sys.exit()

print('IP address of ' + host + ' is ' + remote_ip)
s.connect((remote_ip, port))
print('Socket connected to ' + host + ' on ip ' + remote_ip)