# Sample 4
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

message = 'GET / HTTP/1.1\r\n\r\n'
try:
	s.sendall(message.encode("UTF8"))
except socket.error:
	print('Send failed!')
	sys.exit()
print('Message sent successfully.')

reply = s.recv(4096) # 4096 is the buffer size
print(reply)
s.close()

# Yes, you'll probably get a 400 bad request ... he's not sure why. 