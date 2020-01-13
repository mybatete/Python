from Queue2 import Queue2

myQueue = Queue2()

print myQueue.size()
myQueue.dequeue()

myQueue.traversal()	
myQueue.rev_traversal()	

NUM=10

i=0
while i<NUM:
	name = raw_input("Enter A name: ")
	myQueue.enqueue(name)
	i += 1

myQueue.traversal()	

myQueue.dequeue()
myQueue.dequeue()

myQueue.traversal()	


print myQueue.getFront().getData()
print myQueue.getHead().getData()

exit()

print myQueue.size()

myQueue.traversal()	
myQueue.rev_traversal()	

myQueue.dequeue()


for value in xrange(1,NUM): 

	myQueue.enqueue(value)

print myQueue.size()

myQueue.traversal()	
myQueue.rev_traversal()	

myQueue.search(99)

print "Done search"
myQueue.index(5)
print "Done index"

myQueue.search(12)
myQueue.index(12)

while not myQueue.isEmpty():
	current = myQueue.dequeue()	

	print current.getData()

exit()


