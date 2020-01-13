import random
from ListNode import Node
from unorderedList import UnorderedList


NUM= 20

myList = UnorderedList()

for i in xrange(NUM): 

	value = random.randint(1,100)
	#temp = Node(value)
	
	#print temp, temp.getData()

	myList.add(value)

#exit()

print myList.size()	
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


