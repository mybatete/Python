def main():

	myList=[11,5,78,3,14,67,22,37,19,25,99]
	#myList=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

	print "Before Sort: ",myList

	myList = selectionSort(myList)

	print "\n\nAfter Sort: ",myList

	print "\n\n"


def selectionSort(myList):

	print "\n"
	current = 0
	last = len(myList) - 1

	while current < last :

		least = current

		index = current + 1

		print "Pass:", current, "\n"

		while ( index <= last):
			if myList[index] < myList[least] :
				print "New Minimum: %d Old Minimum: %d Index: %d\n" % (myList[index], myList[least],index)
			 	least = index

			index = index + 1

		#Swap Values:
		tmp             = myList[current]		
		myList[current]	= myList[least]	
		myList[least]	= tmp	

		print myList, "\n"

		current = current + 1

	return myList

main()
