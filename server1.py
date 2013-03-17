import socket               # Import socket module
import pickle
import csv
import select
import random
import os
import sys, string
from thread import*
import time
import threading
from datetime import datetime
from Random_Database import randomDB
lock = threading.Lock()

logfile=open('logfile.txt','w')
s=socket.socket()		
host = socket.gethostname() # Get local machine name
port = 12345	             # Reserve a port for your service.

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
logfile.write('Log Entry for :')
sdate=str(datetime.now())
logfile.write(sdate)
logfile.write('\n\n')
ls=[]
name=[]
gender=[]
bd=[]
dd=[]
region=[]
ac=[]
on=[]
dt={'name':name,'gender':gender,'birth_date':bd,'death_date':dd,'region':region,'achievements':ac,'other_names':on}
def names(n):
	'''Displays names of freedom fighters'''
	z=0
	while z!=n:
		c.send(dt['name'][z])
		c.send('\n')
		z=z+1

def gender1(gen):
	'''Checks the gender given in command line'''
	i=0
	j=-1
	if gen=='Female' or gen=='female':
		for i in dt['gender']:
		        j=j+1
			if i==gen:
				c.send('\n')
				c.send(dt['name'][j])
				c.send('\n')
				c.send(dt['gender'][j])
				c.send('\n')

def achieve(ach,num1):
	'''Displays the name and achievements of freedom fighters'''
	p=0
	for q in dt['region']:
		while p!=num1:
			if q=='india' or q=="southindia" or q=="northindia" or q=='india':				
					c.send('\n')				
					c.send(dt['name'][p])
					c.send("\n")
					c.send(dt['achievements'][p])
					c.send("\n")
					p=p+1

			
def region1(reg):
	'''Checks if the region given in command line argument is same as in the dictionary and displays only those names'''
	x=-1
	if reg=='southindia' or reg=='SouthIndia' or reg=='southIndia':
		for k in dt['region']:
			x=x+1
			if k==reg or k=="southindia" or k=="SouthIndia" or k=="southIndia":
				c.send('\n')
				c.send(dt['name'][x])
				c.send('\n')
				c.send(dt['region'][x])
				c.send('\n')


def det(num):
	"""Displays the details of freedom fighters"""
	y=0
	while y!=num:
		c.send('\n')
		c.send("Name: ")
		c.send(dt['name'][y])
		c.send("\n")
		c.send("Gender: ")
		c.send(dt['gender'][y])
		c.send("\n")
		c.send("Birth Date: ")
		c.send(dt['birth_date'][y])
		c.send("\n")
		c.send("Death Date: ")
		c.send(dt['death_date'][y])
		c.send("\n")
		c.send("Region: ")
		c.send(dt['region'][y])
		c.send("\n")
		c.send("Achievements: ")
		c.send(dt['achievements'][y])
		c.send("\n")
		c.send("Other Names: ")
		c.send(dt['other_names'][y])
		c.send("\n")
		c.send("\n")
		y=y+1
	
def clientthread(c,argv):
	global lock
	lock.acquire()
	flagn=0
	flagg=0
	flagr=0
	flagd=0
	flagt=0
	flagf=0
	flaga=0
	flage=0

	rec=0
	gen=0
	reg=0
	num=0
	n=0
	ach=0 	

	#reading comma seperated values from a file
	q=0
	f=open("database.txt","r")
	reader = csv.reader(f)
	for line in reader:
		rec=rec+1
		ls.extend(line) 

	#taking the input from a file into seperate lists
	for q in range(0,len(ls),7):
		name.append(ls[q])

	for q in range(1,len(ls),7):
		gender.append(ls[q])

	for q in range(2,len(ls),7):
		bd.append(ls[q])

	for q in range(3,len(ls),7):
		dd.append(ls[q])

	for q in range(4,len(ls),7):
		region.append(ls[q])

	for q in range(5,len(ls),7):
		ac.append(ls[q])

	for q in range(6,len(ls),7):
		on.append(ls[q])


	#checking using flags which command line arguments have been given
	for arg in argv:
		if arg=='-n':
			flagn=1
		if arg=='-g':
			flagg=1
		if arg=='-r':
			flagr=1
		if arg=='-d':
			flagd=1
		if arg=='-t':
			flagt=1
		if arg=='-f':
			flagf=1
		if arg=='-a':
			flaga=1
		if arg=='-e':
			flage=1

	#accepting the command line arguments for futher computation
	if flagn==1 and flagg==1 and flagf==1 and flagr==0 and flagd==0 and flagt==0 and flaga==0 and flage==0:
		if argv[2]=='name' and argv[6]=='freedomfighters':
			if argv[4]=='female'or argv[4]=='Female'or argv[4]=='Male' or argv[4]=='male':
				gen=argv[4]
			else:
				c.send("Usage: -g female or -g male")
				gen=0
		else:
			c.send("Usage -n name -g <female or male> -f freedomfighters")


	if flagn==1 and flagr==1 and flagf==1 and flagg==0 and flagd==0 and flagt==0 and flaga==0 and flage==0:
		if argv[2]=='name' and argv[6]=='freedomfighters':
			if argv[4]=='SouthIndia' or argv[4]=='southindia' or argv[4]=='southIndia':
				reg=argv[4]
			else:
				c.send("This is not supported")
				reg=0
					
		else:
			c.send("Usage -n name -r <SouthIndia or southindia or southIndia> -f freedomfighters")
			

	if flagd==1 and flagt==1 and flagf==1 and flagg==0 and flagr==0 and flagn==0 and flaga==0 and flage==0:
		if argv[2]=='details' and argv[6]=='freedomfighters':
			if int(argv[4])<=rec:
				if argv[4].isdigit():
					num=int(argv[4])
				else:
					c.send("Usage: -t <number>")
					num=0
						       
			else:
				c.send("Number of names asked exceeds the number of database records")
				
		else:
			c.send("Usage -d details -t <number> -f freedomfighters")
			
	
	if flagn==1 and flagt==1 and flagf==1 and flagr==1 and flagg==0 and flagd==0 and flaga==0 and flage==0:
		if argv[2]=='name' and argv[8]=='freedomfighters':
			if argv[6]=='india' or argv[6]=='India' or argv[6]=='SouthIndia' or argv[6]=='southindia' or argv[6]=='southIndia' or argv[6]=='NorthIndia' or argv[6]=='northindia' or argv[6]=='northIndia':
				if int(argv[4])<=rec:
					if argv[4].isdigit():
						n=int(argv[4])
					else:
						c.send("Usage: -t <number>")
						n=0
						       		
				else:
					c.send("Number of names asked exceeds the number of database records")
					
			else:
				c.send("This country is not supported")
							 
		else:
			c.send("Usage -n name -t <number> -r <india or southindia or north india> -f freedomfighters")
			

	if flagn==1 and flagr==1 and flaga==1 and flagf==1 and flagt==1 and flagg==0 and flagd==0 and flage==0:
		if argv[2]=='name' and argv[10]=='freedomfighters':
			if argv[8]=='india' or argv[8]=='India':
				if int(argv[6])<=rec:
					if argv[4] and argv[6]:
						ach=argv[4]
						num1=int(argv[6])
					else:
						c.send("Usage: -a achievements -t <number>")
						ach=0
								
				else:
					c.send("Number of names asked exceeds the number of database records")
					
			else:
				c.send("This country is not supported")
						
		else:
			c.send("Usage -n name -a achievements -t <number> -r india  -f freedomfighters")
			
	
	if flage==1 and flagn==0 and flagr==0 and flaga==0 and flagf==0 and flagt==0 and flagg==0 and flagd==0:
		if argv[2]=='end' or argv[2]=='End':
			c.send('Closing the server')
			print "TCP Connection closing...."
			while True:
				abc=select.select([s],'','',1)
				if abc[0]:
					c.send('Closing the server')
					print "TCP Connection closing...."
				else:
					print "Connection closed"
					print 'Thank You'
					s.close()
					logfile.close()      
					os._exit(1)
		else:
			c.send("Usage -e <end or End>")
			
	
	#names of n number of freedom fighters
	if n:
		c.send('List of names of freedom fighters:')
		c.send('NAMES:')
		c.send('\n')
		names(n)

	#names of all female freedom fighters
	elif gen:
		c.send("The names of the female freedom fighters are:")
		c.send("NAMES & GENDER:")
		c.send('\n')
		gender1(gen)

	#names and achievements of all freedom fighters
	elif ach:
		c.send("List of freedom fighters of India and their achievements are:")
		c.send("NAMES & ACHIEVEMENTS:")
		c.send('\n')
		achieve(ach,num1)
	
	#names of all freedom fighters of southern india
	elif reg:
		c.send("NAMES & Region:")
		c.send('\n')	
		region1(reg)
	
	#details of alteast t number of freedom fighters
	elif num:
		c.send("The details of freedom fighters are:")
		c.send('\n')
		det(num)
	
	else:
		c.send("Please enter valid arguments.")
		c.send('\n')	
	lock.release()

while True:
	abc=select.select([s],'','',50)
	if abc[0]:
		c,addr=s.accept()
		print 'Connected to client: ',addr
		#Get address. Not Port Number.
		for i in addr:
			caddress=addr[0]
		cad=caddress
		logfile.write('Client:')
		logfile.write(cad)
		logfile.write('\n')
		logfile.write('Time:')
		cdate=str(datetime.now())
		logfile.write(cdate)
		logfile.write('\n')
		argv=pickle.loads (c.recv(1024))
		logfile.write('Arguments passed by Client')
		st=""
		for ar in argv:
			st=st+" "+ar
		logfile.write(st)
		logfile.write('\n\n')
		start_new_thread(clientthread,(c,argv))
	else:
		c.close()
		logfile.close()
	
