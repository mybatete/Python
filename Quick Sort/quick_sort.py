MINSIZE=4

def main():

	myList=[11,5,78,3,14,67,22,37,19,25,99]
	#myList=[15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

	print "Before Sort: ",myList

	left  = 0
	right = len(myList)-1

	myList = quickSort(myList,left,right)

	print "\n\nAfter Sort: ",myList

	print "\n\n"


def quickInsertion(myList,first,last):

	#print "\n"
	current = first + 1
	
	#last = len(myList) - 1

	while current <= last :

		value = myList[current]

		index =  current - 1

		#print "Pass:", current, "\n"

		while ( index >=first and value < myList[index]):
			#print "Index: %d ... Comparing %d\t%d\n" % (index, value, myList[index])
		
			myList[index + 1] = myList[index]
			index             = index -1

		myList[index + 1] = value

		#print myList, "\n"

		current = current + 1

	return myList

def medianLeft(myList,left,right):

	mid = (left + right)/2

	# Compare Left and Middle:
	if myList[left] > myList[mid]:
		tmp           = myList[left]
		myList[left]  = myList[mid]
		myList[mid]   = tmp

	# Compare Left and Right:
	if myList[left] > myList[right]:
		tmp           = myList[left]
		myList[left]  = myList[right]
		myList[right] = tmp

	# Compare Middle and Right:
	if myList[mid] > myList[right]:
		tmp           = myList[mid]
		myList[mid]   = myList[right]
		myList[right] = tmp

	# Swap Left and Median:
	tmp          = myList[left]
	myList[left] = myList[mid]
	myList[mid]  = tmp

	return


def quickSort(myList,left, right):

	if (right - left) > MINSIZE:
 
		medianLeft(myList,left,right)

		pivot     = myList[left]
		sortLeft  = left + 1
		sortRight = right

		while sortLeft <= sortRight:

			while myList[sortLeft] < pivot :

				sortLeft += 1

			while myList[sortRight] >= pivot :

				sortRight -= 1

			if sortLeft <= sortRight :
				#Swap:
				tmp               = myList[sortLeft]
				myList[sortLeft]  = myList[sortRight]
				myList[sortRight] = tmp

		myList[left]         = myList[sortLeft -1]
		myList[sortLeft -1 ] = pivot

		if left < sortRight:
			quickSort(myList, left, sortRight-1)

		if sortLeft < right:
			quickSort(myList, sortLeft, right)

	else:
		quickInsertion(myList,left, right)	

	return myList

main()
