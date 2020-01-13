"""
Program:Binary Search engine
author: Batete Yedidia Marc
date:09/06/2018
description: the program prompts the user to enter the name of a patient, then checks inside the Patients file to see if the name is in there.
input:
    -file Patient_info-sorted.dat
    -patients name(search)
output:
    -patients record
    -number of iterations
"""
from Patients import patients #imports the class from which we can create and manipulate objects
fg = open ("Patient_info-sorted.dat","r") #opens the file to read from

search = raw_input ("enter a search: ")# the program prompts the user to enter a value to search

l =[]
fg.readline()
while True:
    line = fg.readline()
    if line =="":
        break
    line = line.strip()
    word = line.split()
    name = word[0] #the program iterates through the file
    contact = word[1]
    age = int(word[2])
    days = int(word[3])
    balance = float(word[4])

    s = patients(name, contact, age, days, balance) #the program creates objects 

    l.append(s)#the program appends the objects to the list
first = 0
last = 999
pos1  = l[first].getName()
pos2 = l[last].getName()
mid = 455
count = 0
while (first <= last): #the program compares the last value
	mid = (first+last)/2
	count+=1
	if (search> (l[mid].getName())):#the program compares the last value of the search to the mid value if it's superior, the mid value becomes first
		first = mid+1
	elif (search < (l[mid].getName())):#the program compares the last value of the search to the mid value if it's inferior, the mid value becomes last
		last = mid-1
	else:
				break

if(search == (l[mid].getName())):#the program outputs the resut of the search and the number of time it ran 
	print "found!", l[mid].getName(), l[mid].getContact(), l[mid].getAge(), l[mid].getDays(), l[mid].getBalance()
	print "the program searched ", count, "times"
else:
	print "Patient records not found"


