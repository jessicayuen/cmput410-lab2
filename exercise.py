# Copyright (c) 2015 Jessica Yuen <jyuen@ualberta.ca>
# 
# Licensed under the GNU General Public License, Version 3.
# A copy of this license is provided with this program. 
# Please consult that or visit: <http://www.gnu.org/licenses/gpl.html> 
#
# run python exercise.py

import socket
import sys
import threading

class ClientThread(threading.Thread):

	def __init__(self, conn):
		super(ClientThread, self).__init__()
		self.running = True
		self.conn = conn

	def run(self):
		while True:
			data = self.conn.recv(1024)

			if data.rstrip() == chr(27).encode():
				break

			# To the TA: Please note that I do not need to trim the string
			# here as in my python environment, the extra characters are 
			# not being displayed.
			# i.e. typing 
			#	Hello
			# will echo 
			#	Hello Jessica
			# and NOT what was seen in the lab of
			# 	\bHello Jessica\r\n
			reply = str(data).rstrip() + ' Jessica\n'
			self.conn.sendall(reply.encode('UTF8'))

		self.conn.close()

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
	print('Failed to create socket!')
	print('Error code: ' + str(msg[0]) + ', error message: ' + msg[1])
	sys.exit()

print('Socked created successfully.')

host = ''
port = 8888

try:
	s.bind((host, port))
except socket.error:
	msg = str(socket.error)
	print('Bind failed! Error code: ' + str(msg[0]) + ', message: ' + msg[1])
	sys.exit()

print('Socket bind complete.')
s.listen(10)
print('Socket is now listening.')

while True:
	conn, addr = s.accept()

	print('Connected with ' + addr[0] + ':' + str(addr[1]))
	thread = ClientThread(conn)
	thread.start()

s.close()