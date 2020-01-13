import sys

from ListNode import Node
from unorderedList import UnorderedList

SHORT  = 200
MEDIUM = 1000

jobListShort  = UnorderedList()
jobListMedium = UnorderedList()
jobListLong   = UnorderedList()

try:
	fp = open("processor_jobs.dat", "r")

except IOError:
	sys.exit("\n\n\nUnable to Open File!!!\n\n\n")

while True:
	line = fp.readline()
	if line == "":
		break
	
	line    = line.strip()
	field   = line.split()
	data	=float(field[0])

	if data <= SHORT:
		jobListShort.add(data)

	elif data <= MEDIUM:
		jobListMedium.add(data)

	else:
		jobListLong.add(data)

	
#jobListShort.traversal()

print "Number of Process in Short Linked List  :", jobListShort.size()

print "Number of Process in Medium Linked List :", jobListMedium.size()

print "Number of Process in Long Linked List   :", jobListLong.size()

#print "Total execution Time is: ", jobListShort.Sum()

		
