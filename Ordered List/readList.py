
from ListNode import Node
from orderedList import orderedList

intList=orderedList()

while True:

	value = raw_input("Enter an integer value: ")

	if value =="":
		break
	
	intList.add(int(value))

	
print "Printing Integers in Ordered Linked List: "
intList.traversal()
