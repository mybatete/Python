"""
Program: seqBinSearch.py
Author : Charles Addo-Quaye
E-mail : caaddoquaye@lcsc.edu
Date   : 01/31/2018 

Description: 
This program implements demo for both
sequential and binary search algorithms. 

The program generates a random list of integers
and provides a menu for searching for numbers
in the list. 

Input variables: List
Output variables: match, found 

"""

import random

def main():
	
	NUM=100
	List = []

	for num in xrange(NUM):
		value = random.randint(0,50000)
		List.append(value)

	size  = len(List)

	print List

	List.sort()
	#print List

	print "\n\nListed Database contains %d Records\n\n" % len(List)  
	
	#Create a List to store the returned Found item: 
	match = []
	done = False

	while not done:
		response = raw_input("Exit Records Database? 'Y/N': ")
		if response.upper() == "Y":
			done  = True
		else:
			query = input("Enter a Number: ")
			found = seqSearch(List,size,query,match)
			#found = binarySearch(List,size,query,match)

			if found:
				print "Query Number (%d) Found: %d at Position: %d\n" % (query, match[0],match[1])
			else:
				print "\n\n***No Record of the Number %s in Database***\n\n" % query
	


def binarySearch(List,size,query,match):

	i     = 0
	first = 0
	last  = size - 1

	found = False
	while first <= last :

		mid = (last + first)/2
		print "Search iteration: %d\tMid-point: %d" % (i,mid)
		i = i + 1

		if query > List[mid]:

			first = mid + 1

		elif query < List[mid]:
			last = mid - 1
		else:
			break
			#first = last  + 1
			#last  = first - 1

	if query == List[mid]:
		found = True
		match.insert(0,List[mid])
		match.insert(1,mid)

	return found


def seqSearch(List,size,query,match):

	i = 0
	found = False
	while i < size and query != List[i]:
		print "Search iteration: %d" % (i)
		i = i + 1	

	if i < size and query == List[i]:
		found = True
		match.insert(0,List[i])
		match.insert(1,i)

	return found

main()

