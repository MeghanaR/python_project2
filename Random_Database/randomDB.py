import string 
import random 
import time
import timeit

def randomBirthDate():
	'''Function to generate random birth date'''
	d=list(range(1,32))
	m=list(range(1,13))
	y=list(range(1900,1931))
	p=random.randint(0,30)
	q=random.randint(0,11)
	r=random.randint(0,29)

	return str(d[p])+"/"+str(m[q])+"/"+str(y[r])

def randomDeathDate():
	'''Function to generate random death date'''
	d=list(range(1,32))
	m=list(range(1,13))
	y=list(range(1940,1981))
	p=random.randint(0,30)
	q=random.randint(0,11)
	r=random.randint(0,39)

	return str(d[p])+"/"+str(m[q])+"/"+str(y[r])

def achieve():
	'''Function to generate Achievements'''
	lt=[]
	achstr=''
	n=random.randint(1,5)	
	for m in range(0,n):
		i=random.randint(0,11)
		setofach=['Bravery Award','Fought for India\'s Independence','Formed the Constitution of India','Free Democratic India','Ranjit Award','Talent Award','Archery Award','Best Fighter Award','Gold Award','Best Ruler','Patriotic Award','Social Award']
		ach=setofach[i]
		lt.append(ach)
	for st in lt:
		achstr=achstr+st+';'
        return achstr

def gender1(nam):
	'''function to generate gender'''
	if nam == 'Ayesha':
		gender= 'female'
	elif nam == 'Meghana':
		gender= 'female'
	elif nam == 'Geetha':
		gender= 'female'
	elif nam == 'Roopa':
		gender= 'female'
	elif nam == 'Deepti':
		gender= 'female'
	elif nam == 'Pooja':
		gender= 'female'
	else:
		gender= 'male'
	return gender

def region1():
	'''function to generate region'''	
	n= random.randint(0,2)
	if n==0:
		reg= 'southindia'
	elif n == 1:
		reg= 'northindia'
	else:
		reg= 'india'
	return reg

def other(gen):
	'''funcion to generate random other names'''
	ot=[]
	achstr=''
	num=random.randint(0,2)
	for x in range(0,num):
	
		if gen== 'female':
			n=random.randint(0,3)
			otherf=['Nightingale of India','Godmother','Jhansi Ki Rani','Mother Of the Nation','Name 1']
			othern=otherf[n]
		else:
			n=random.randint(0,10)		
			otherf=['Raja','Manmohan','Mahatma Gandhi','Subash Chandra Bose','Chacha','Babu','Bapu','Father of the Nation','Godfather','King','Mahatma']	
			othern=otherf[n]
		ot.append(othern)
	for st in ot:
		achstr=achstr+st+';'
	return achstr	

def RandomName():
	'''funcion to generate random names'''
	first=['Ram','Anand','Ayesha','Meghana','Krishna','Geetha','Roopa','Dheeraj','Nitin','Deepti','Pooja','Aditya','Avinash','Suraj','Madhur','Prashant']
	middle=['H','Kumar','M','B','K','P','Kumari','N','R','A','S','V','D','T','I']
	last=['Agarwal','Raman','Iyer','Das','Tagore','Lal','Naidu','Gandhi','Bose','Murthy','Gupta','Mishra','Bhat','Singh','Sharma']
	i=random.randint(0,14)
	j=random.randint(0,14)
	k=random.randint(0,14)
	name=''
	name=first[i]+' '+middle[j]+' '+last[k]
	return first[i],name
	

fp=open("database.txt","w")
size = random.randint(5,10) #size of characters
rec=raw_input('Enter the number of entries to be made in the database\n')

starttime=time.clock()

for x in range(0,int(rec)):
	first1,nam=RandomName()
	gen=gender1(first1)
	bd=randomBirthDate()
	dd=randomDeathDate()
	reg=region1()
	ach=achieve()
	oth=other(gen)	
	
	fp.write(nam+','+gen+','+bd+','+dd+','+reg+','+ach+','+oth+'\n')

fp.close()

endtime=time.clock()
totaltime=endtime-starttime;
print 'The amount of time taken to build the database: ', totaltime, ' seconds.'
	
