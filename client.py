import socket               # Import socket module
import getopt,sys
import pickle
import os
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345              # Reserve a port for your service.
s.connect((host, port))


#taking command line arguments
optlist,args=getopt.getopt(sys.argv,'ngdtarf:')
pickledList=pickle.dumps(sys.argv)
s.send(pickledList)
while True:
	abc=select.select([s],'','',1)
	if abc[0]:
		data = s.recv(1024)
		print data
	else:
		print 'Thank You'
		s.close()      
		os._exit(1)
