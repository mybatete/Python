from ListNode import Node

class UnorderedList:

	def __init__(self):
		self.head = None

	def getHead(self):
		return self.head

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp      = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count    = 0
	
		while current != None:

			count += 1
			current = current.getNext()

		return count

	def append(self,item):
		current = self.head

		if current == None:
			temp      = Node(item)
			temp.setNext(self.head)
			self.head = temp
			
		else:
			while current.getNext() != None:
				current = current.getNext()
			
			temp = Node(item)
			current.setNext(temp)



	def remove(self,item):
		current  = self.head
		previous = None
		count    = 0
		found    = False

		print "Searching List for item", item
		while current != None:

			if current.getData() == item:
				print "Item Found: ",current.getData(), "at location:", count
				found = True
				break
			
			previous = current
			current  = current.getNext()
			count   += 1
		
		if found:
			
			print "Removing item: ", item 		
			if previous != None:
				new_next  = current.getNext()
				previous.setNext(new_next)
			else:
				self.head = current.getNext() 

		else:
			print "Item: ", item, "Was Not Found On List"

		return found

	def index(self,item):
		current  = self.head
		position = 0
		found    = False

		print "Searching List for item", item
		while current != None:

			if current.getData() == item:
				print "Item Found: ",current.getData(), "at location:", position
				found = True
				break

			current   = current.getNext()
			position += 1

		if not found:
			print "Item: ", item, "Was Not Found On List"
			position = -1

		return position

	def search(self,item):
		current = self.head
		count   = 0
		found   = False

		print "Searching List for item", item
		while current != None:

			if current.getData() == item:
				print "Item Found: ",current.getData(), "at location:", count
				found = True
				break

			current = current.getNext()
			count  += 1

		return found

	def traversal(self):
		current = self.head
		count    = 1
	
		while current != None:

			print count, hex(id(current)),current.getData()
			current = current.getNext()
			count += 1

	def Sum(self):
		current = self.head
		count          = 1
		total_time     = 0
		while current != None:

			total_time += current.getData()
			print count, hex(id(current)),current.getData()
			current = current.getNext()
			count += 1
		
		return total_time
			

