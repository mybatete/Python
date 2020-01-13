def main():

	#myList=[11,5,78,3,14,67,22,37,19,25,99]
	myList=[99,22,78,3,14,67,5,37,19,25,11,4,2]
	#myList=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

	print "Before Sort: ",myList

	myList = shellSort(myList)

	print "\n\nAfter Sort: ",myList

	print "\n\n"


def shellSort(myList):

	print "\n"
	last = len(myList) - 1

	size = last / 2

	while size != 0 :

		current = size

		while current <= last :

			value = myList[current]

			index =  current - size

			while ( index >=0 and value < myList[index]):
				print "Size: %d Current: %d Index: %d ... Comparing %d\t%d\n" % (size, current,index, value, myList[index])
		
				myList[index + size] = myList[index]
				index                = index - size

			myList[index + size] = value

			print myList, "\n"

			current = current + 1

		print myList, "\n"

		size = size / 2
		

	return myList

main()
