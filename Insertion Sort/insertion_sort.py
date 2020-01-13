def main():

	myList=[11,5,78,3,14,67,22,37,19,25,99]
	#myList=["James","Mark","Tomas","Zac","Tim","Jane","Elizabeth","Mary","John","Ethan"]

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
			#print "Index: %d ... Comparing %s\t%s\n" % (index, value, myList[index])
		
			myList[index + 1] = myList[index]
			index             = index -1

		myList[index + 1] = value

		print myList, "\n"

		current = current + 1

	return myList

main()
