import random
from ListNodeDL import Node
from orderedListDL import orderedListDL


NUM= 20

myList = orderedListDL()

for i in xrange(NUM): 

	value = NUM - i
	print value
	#value = random.randint(i)
	#temp = Node(value)
	
	#print temp, temp.getData()

	myList.add(value)

print myList.size()
size = myList.size()

myList.traversal()	
myList.rev_traversal()	


myList.add(-1)
myList.add(21)
myList.add(44)

myList.search(99)

print "Done search"
myList.index(99)
print "Done index"
myList.remove(99)
print "Done remove"

myList.search(12)
myList.index(12)
myList.remove(12)
myList.traversal()	

myList.remove(-1)
myList.traversal()	
myList.remove(4)
myList.traversal()	
myList.remove(44)
myList.traversal()	
myList.rev_traversal()	
exit()
	
myList.traversal()	
myList.add(99)
myList.add(75)
myList.add(92)

print

myList.search(99)
myList.search(62)

myList.remove(70)
myList.traversal()	

myList.remove(99)
myList.traversal()	

myList.remove(92)
myList.traversal()	

myList.append(5)
myList.append(15)
myList.append(25)
myList.traversal()	

myList.index(5)
myList.index(25)

'''
myList.append(5)
myList.append(15)
myList.append(25)
myList.traversal()	

exit()
'''


