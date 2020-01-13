#Problem is also called the Josephus Problem:
from Queue2 import Queue2

def main():

	#Create an Queue Object:
	myQueue = Queue2()

	#Create a List of Names:
	names   = createNameList()

	#Insert Names in the Queue
	for name in names:
		myQueue.enqueue(name)		


	myQueue.traversal()
	print myQueue.size()

	ROUNDS=int(input("\n\nInput the number of rounds: \n"))

	#While there is more than 1 person in the queue:
	while myQueue.size() > 1 :

		#Pass potato around "ROUNDS" times
		for i in xrange(ROUNDS):
			current = myQueue.dequeue()
			person  = current.getData()
			print person
			myQueue.enqueue(person)

		#Remove Person holding the potato after passing around:	
		current = myQueue.dequeue()
		person  = current.getData()
		print "\n\n"
		print "Terminated: ", person
		print "Crime     : Caught Holding A Hot Potato !!!"
		print "\n\n"
		raw_input()

	#Display the name of the last person remaining in the queue:
	current  = myQueue.getFront()
	survivor =  current.getData()
	print "\n\n\n\n"
	print "Survivor: ",survivor, "!!!!!"
	print "\n\n\n\n"

def createNameList():

	print "\n\nCreating Player List For Hot Potato Simulation\n\n" 


	names = []
	NUMP    = int(input("Enter the Number of Participants: "))

	i = 0

	while i < NUMP:	
	
		name = raw_input("Enter A Name: ")
		names.append(name)
		i   += 1
		
	return names


main()

exit()

