def main():

	myList=[11,5,78,3,14,67,22,37,19,25,99]
	#myList=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

	print "Before Sort: ",myList

	myList = insertionSort(myList)

	print "\n\nAfter Sort: ",myList

	print "\n\n"


def insertionSort(myList):

	print "\n"
	current = 1
	last = len(myList) - 1

	while current <= last :

		value = myList[current]

		index =  current - 1

		print "Pass:", current, "\n"

		while ( index >=0 and value < myList[index]):
			print "Index: %d ... Comparing %d\t%d\n" % (index, value, myList[index])

			raw_input()
		
			myList[index + 1] = myList[index]
			index             = index -1

		myList[index + 1] = value

		print myList, "\n"

		current = current + 1

	return myList

main()
