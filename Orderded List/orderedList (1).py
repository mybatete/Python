from ListNode import Node

class orderedList:

	def __init__(self):
		self.head = None

	def getHead(self):
		return self.head

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		print "Adding ..."
		# Case 1: List is Empty:
		if self.head == None:
			temp      = Node(item)
			temp.setNext(self.head)
			self.head = temp
		else:
			current  = self.head
			previous = None

			while current != None:
				if current.getData() > item:
					break

				previous = current
				current  = current.getNext()
			
			temp        = Node(item)
			
			# Case 2: Item is to be inserted before first
			#         item on the List: So previous is None
			if previous == None:
				temp.setNext(self.head)
				self.head = temp
			
			# Case 3: Inserting into Middle or End:
			else:
				#temp.setNext(previous.getNext())
				temp.setNext(current)
				previous.setNext(temp)


	def size(self):
		current = self.head
		count    = 0
	
		while current != None:

			count += 1
			current = current.getNext()

		return count


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
			
			if current.getData() > item:
				found = False
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

			if current.getData() > item:
				found = False
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

			print "Comparing: ",current.getData(), "Item", item
			if current.getData() == item:
				print "Item Found: ",current.getData(), "at location:", count
				found = True
				break

			if current.getData() > item:
				found = False
				break

			current = current.getNext()
			count  += 1

		if not found:
			print "Item: ", item, "Was Not Found On List"

		return found

	def traversal(self):
		current = self.head
		count    = 1

		print "Traversing List ..."	
		while current != None:

			print count, hex(id(current)),current.getData()
			current = current.getNext()
			count += 1

