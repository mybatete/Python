"""
Program:sorting list
author: Batete Yedidia Marc
date:09/01/2018
description: the program searches through the given file and makes it easier to access.
input:
    -file Patient_info.dat
    -patients name(search)
output:
    -patients record
    
"""
from Patients import patients

fg = open ("Patient_info.dat","r")

l =[]
fg.readline()
while True:
    line = fg.readline()#the program reads the file line per line
    if line =="":
        break
    line = line.strip()
    word = line.split()
    name = word[0]
    contact = word[1]
    age = int(word[2])
    days = int(word[3])
    balance = float(word[4])

    s = patients(name, contact, age, days, balance) #the program Makes a object with the parts from the filw

    l.append(s)#the program adds the objects into a list
r = patients("Elizabeth", "814-227-2397", 23, 5, 250.00)
s  = patients("James", "302-324-7795", 45, 12, 1984.23)
l.append(s) #the given records are added as object to the list l
l.pop(15)
k = patients("connor", "408-746-9371 ", 11, 7, 600.55)
l.insert(14,k)

for item in l:
    a = item.getAge()
    if a >=65:
        print "before ", item.getBalance(), item.getAge()
        item.updateBalance(10)
        print item.getBalance()
#A discount of 10% is applied to all the patients whose age is over 65.

for item in l:
    a = item.getAge()
    if (a >= 85):
        print a
        l.remove(item)
for item in l:
        
    print item.getName(), item.getContact(), item.getAge(), item.getDays(), item.getBalance()

