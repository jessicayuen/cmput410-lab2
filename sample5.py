# Sample 5
import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
	print('Failed to create socket!')
	print('Error code: ' + str(msg[0]) + ', error message: ' + msg[1])
	sys.exit()

print('Socked created successfully.')

# Part 1
host = ''
port = 8888

try:
	s.bind((host, port))
except socket.error:
	msg = str(socket.error)
	print('Bind failed! Error code: ' + str(msg[0]) + ', message: ' + msg[1])
	sys.exit()

print('Socket bind complete.')
s.listen(10) # Limitation to number of connections that can be in the queue
print('Socket is now listening.')
conn, addr = s.accept()	# blocking call, to accept the first client that comes
print('Connected with ' + addr[0] + ':' + str(addr[1]))

# can type in bash the following to talk to the socket: telnet localhost 8888

# Part 2

data = conn.recv(1024)
reply = '<<<Hello ' + str(data) + '>>>'
conn.sendall(reply.encode('UTF8')) 

# once you start the socket with python sample5.py
# try telnet localhost 8888 in another terminal
# type test, and it should echo back <<<Hello test>>>

conn.close()
s.close()