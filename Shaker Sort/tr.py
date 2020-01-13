def main():

	myList=[11,5,78,3,14,67,22,37,19,25,99]
	#myList=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

	print "Before Sort: ",myList

	myList = ShakerSort(myList)

	print "\n\nAfter Sort: ",myList

	print "\n\n"


def ShakerSort(myList):

	print "\n"
	current = 0
	Sorted  = False
	last    = len(myList) - 1
	

	while current <= last and Sorted==False :

		Sorted = True
		index  = last

		print "Pass:", current, "\n"

		while ( index > current):
			if myList[index] < myList[index-1] :
				print "Swapping: %d And : %d\n" % (myList[index], myList[index-1])
				Sorted = False
		
				#Swap Values:
				tmp             = myList[index]		
				myList[index]	= myList[index-1]	
				myList[index-1]	= tmp	


			index = index - 1

		print myList, "\n"

		current = current + 1
		index = 0
		while ( current < last):
			if myList[index] > myList[index+1] :
				print "Swapping: %d And : %d\n" % (myList[index], myList[index+1])
				Sorted = False
		
				#Swap Values:
				tmp             = myList[index]		
				myList[index]	= myList[index+1]	
				myList[index+1]	= tmp	


			index = index + 1

		print myList, "\n"

		current = current + 1


	return myList

main()
