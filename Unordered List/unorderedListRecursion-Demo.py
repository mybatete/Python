import random
from unorderedList import UnorderedList

NUM= 10

def main():

	myList = UnorderedList()

	for i in xrange(NUM): 

		value = random.randint(1,100)
	
		myList.add(value)

	print"\n\nPrinting in List...\n"
	myList.traversal()

	print"\n\nPrinting in Reverse...\n"
	printReverse(myList.head)

	return

def printReverse(current):
        
	if current == None:
		return

	else:
		printReverse(current.getNext())
		print hex(id(current)),current.getData()

	return


main()
