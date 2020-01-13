def main():

	fp     = open("readings.dat", "r")
	fpOut  = open("readings_ascending-order.dat", "w")
	myList = []

	while True:
		line = fp.readline()

		if line =="":
			break

		line = line.strip()
		word = line.split()
		myList.append(float(word[0]))


	print "Before Sort: ",myList

	myList = insertionSort(myList)

	for value in myList:
		fpOut.write("%.2f\n" % (value))

	print "\n\nAfter Sort: ",myList

	print "\n\n"


def insertionSort(myList):

	#print "\n"
	current = 1
	last = len(myList) - 1

	while current <= last :

		value = myList[current]

		index =  current - 1

		#print "Pass:", current, "\n"

		while ( index >=0 and value < myList[index]):
			#print "Index: %d ... Comparing %d\t%d\n" % (index, value, myList[index])
			#print "Index: %d ... Comparing %s\t%s\n" % (index, value, myList[index])
		
			myList[index + 1] = myList[index]
			index             = index -1

		myList[index + 1] = value

		#print myList, "\n"

		current = current + 1

	return myList

main()
