"""
Program: snow calculator
author: Batete Yedidia Marc
date:09/18/2018
description: the progrgam reads from a file containing data about the annual snowfall and
manages the data to make it easier to manipulate.
input:
    -file Annual_Snow_Falls.dat
    
output:
    average inches of fall
    total number of collision
"""
import sys
fp = open ("Annual_Snow_Falls.dat","r")
maxa = 17389 
liste = [None]*maxa
i = 0
collisions = 0
probes = 0
fp.readline()
# loop trough the file
while True:
    #read line of the file
    line = fp.readline()
    if line == "":
        break
    line = line.strip()
    field = line.split()
    key = int(field[1])
    #create the address
    address = key % maxa
    #check if the address is empty
    if liste[address] !=None:
        collisions +=1

    k = 1
    while liste[address] !=None and address < maxa:
        probes +=1
        address += k*k
        k += 1
        print "on est entree en colusion"

    if liste[address] != None or address >= maxa:
        print "unresolved for ", key

    else:
        liste[address] = field
        print liste[address]
        print liste[address][0]
        i = i+1
print probes
print collisions
print i
done = False

while not done:
    #ask the user if they want to exit the database
    response = raw_input("exit Records Database? 'y/n': ")
    if response. upper() =="Y":
        done = True
    else:
        # ask the user to enter a key to search
        key = input("enter the key: ")
        #makes a key with the remainder from the division of the key with the max
        address = key % maxa

        k = 1
        while liste[address][1] !=str(key) and address< maaxa:
            address += k *k
            k = k + 1
        if liste[address][1] != str(key) or address >= maxa:
            exit()
        else:
            print liste[address]
            summ = float(liste[address][2])+float(liste[address][3])+float(liste[address][4])+float(liste[address][5])+float(liste[address][6])
            average = summ/5.0
            print "average = ", average
            h = 0
            for x in xrange (2,6):
                if float(liste[address][x])>h:
                    h = float(liste[address][x])
            print  "the maximum of the snow falls is: " ,h 
                
            
    
