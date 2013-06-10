class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.parent = None
		self.data = data

	def insert(self, data):
		if self == None:
			self = Node(data)
		else:
			if data < self.data:
				if self.left == None:
					self.left = Node(data)
				else:
					self.left.insert(data)
				self.left.parent = self
			else:
				if self.right == None:
					self.right = Node(data)
				else:
					self.right.insert(data)
				self.right.parent = self

	def lookup(self, data, parent=None):
		if data < self.data:
			if self.left == None:
				return None, None
			return self.left.lookup(data, self)
		elif data > self.data:
			if self.right == None:
				return None, None
			return self.right.lookup(data, self)
		else:
			return self, parent

	def preorder(self):
		print self.data
		if self.left:
			self.left.preorder()
		if self.right:
			self.right.preorder()

	def inorder(self):
		if self.left:
			self.left.inorder()
		print self.data
		if self.right:
			self.right.inorder()

	def postorder(self):
		if self.left:
			self.left.postorder()
		if self.right:
			self.right.postorder()
		print self.data


bst = Node(2)
bst.insert(4)
bst.insert(6)
bst.insert(13)
bst.insert(20)
bst.insert(21)
bst.insert(9001)
bst.preorder()
bst.inorder()
bst.postorder()
node, parent = bst.lookup(21)

print node.data, parent.data
