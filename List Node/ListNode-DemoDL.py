import random
from ListNodeDL import Node

NUM= 20

nodes=[]

for i in xrange(NUM): 

	value = random.randint(1,100)
	temp = Node(value)
	
	print hex(id(temp)), temp.getData()

	nodes.append(temp)

#print nodes

#print hex(id(nodes[2]))

nodes[2].setPrev(nodes[1])
nodes[2].setNext(nodes[3])

print nodes[2].getPrev()
print nodes[2].getNext()

print nodes[2].getPrev().getData()
print nodes[2].getNext().getData()




