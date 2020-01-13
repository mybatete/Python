import random
#from QueueNode import Node
from Queue2 import Queue2


NUM= 21

myQueue = Queue2()

print myQueue.size()
myQueue.dequeue()

myQueue.traversal()	
myQueue.rev_traversal()	


myQueue.enqueue(-1)

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


