import random
from Stack import Stack


NUM= 20

myStack = Stack()

print myStack.size()
myStack.pop()

for i in xrange(NUM): 

	value = random.randint(1,100)

	myStack.push(value)

print myStack.size()	
myStack.traversal()	

for i in xrange(NUM): 
	myStack.pop()

myStack.traversal()	
myStack.pop()
myStack.top()

print myStack.isEmpty()


print "Re-stacking ..."

for i in xrange(NUM): 

	value = random.randint(1,100)

	myStack.push(value)

print myStack.size()	
myStack.traversal()	

#exit()


myStack.push(99)
myStack.push(75)
myStack.push(92)

myStack.push("DogHouse")

print


myStack.pop()
myStack.traversal()	

myStack.pop()
myStack.traversal()	

exit()


