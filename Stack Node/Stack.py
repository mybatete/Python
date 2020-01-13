from StackNode import Node

class Stack:

	def __init__(self):
		self.head = None
		self.count=0

	def getHead(self):
		return self.head

	def isEmpty(self):
		return self.head == None

	def push(self, item):
		print "Pushing ... ", item
		temp        = Node(item)
		temp.setNext(self.head)
		self.head   = temp
		self.count += 1

	def size(self):
		return self.count


	def pop(self):
		current  = self.head

		if current == None:
			print "Empty Stack!!!"
			return None
		else:
			print "Popping ... ", current.getData()
			self.head = current.getNext() 
			self.count -= 1
			return current.getData()

	def top(self):
		current  = self.head

		if current == None:
			print "Empty Stack!!!"
			return None
		else:
			print "Top Item: ", current.getData()
			return current.getData()


	def traversal(self):
		current = self.head
		count    = 1
	
		while current != None:

			print count, hex(id(current)),current.getData()
			current = current.getNext()
			count += 1


