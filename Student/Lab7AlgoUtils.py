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


