import sys

from ListNode import Node
from unorderedList import UnorderedList

jobList= UnorderedList()

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

	jobList.add(data)

jobList.traversal()

print "Total execution Time is: ", jobList.Sum()

		
