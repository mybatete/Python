
class BinaryTree(object):

	def __init__(self, root):
		self.key         = root
		self.left_child  = None
		self.right_child = None
   
	def insert_left(self, new_node):
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			t               = BinaryTree(new_node)
			t.left_child    = self.left_child
			self.left_child = t

 
	def insert_right(self, new_node):
		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			t                = BinaryTree(new_node)
			t.right_child    = self.right_child
			self.right_child = t

   
	def get_right_child(self):
		return self.right_child

	def get_left_child(self):
		return self.left_child

	def set_root_val(self, obj):
		self.key = obj

	def get_root_val(self):
		return self.key

   
	def preorder(self):
		print(self.key),

		if self.left_child:
			self.left_child.preorder()

		if self.right_child:
			self.right_child.preorder()

	def inorder(self):
		if self.left_child:
			self.left_child.inorder()

		print(self.key),
	  
		if self.right_child:
			self.right_child.inorder()

   
	def postorder(self):
		if self.left_child:
			self.left_child.postorder()
		if self.right_child:
			self.right_child.postorder()
		print(self.key),

	def find_node(self,value):

		nodeM = nodeL = nodeR = None

		if self.key== value:
			nodeM = self
			print "Found: ", self.key

		if self.left_child:
			nodeL = self.left_child.find_node(value)

		if self.right_child:
			nodeR = self.right_child.find_node(value)

		node = nodeM or nodeR or nodeL
		
		return node


	def find_leaf(self):
		
		if self.left_child==None and self.right_child==None :
			print "Leaf Node:", self.key

		if self.left_child:
			self.left_child.find_leaf()

		if self.right_child:
			self.right_child.find_leaf()

	def mirror(self,mirror_node):
		if self.left_child:
			right_child=self.left_child.get_root_val()
			mirror_node.insert_right(right_child)

			self.left_child.mirror(mirror_node.get_right_child())

		#print(self.key),
	  
		if self.right_child:
			left_child=self.right_child.get_root_val()
			mirror_node.insert_left(left_child)

			self.right_child.mirror(mirror_node.get_left_child())



