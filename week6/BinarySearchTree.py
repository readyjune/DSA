class Node:
	def __init__(self, key, val):
		self.value = val
		self.key = key
		self.leftChild = None
		self.rightChild = None




	def insert(self, key, data):
		if self.key == key:
			return False
		elif self.key > key:
			if self.leftChild:
				return self.leftChild.insert(key, data)
			else:
				self.leftChild = Node(key, data)
				return True
		else:
			if self.rightChild:
				return self.rightChild.insert(key, data)
			else:
				self.rightChild = Node(key, data)
				return True


	def getHeight(self):
		if self.leftChild and self.rightChild:
			return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
		elif self.leftChild:
			return 1 + self.leftChild.getHeight()
		elif self.rightChild:
			return 1 + self.rightChild.getHeight()
		else:
			return 1

	def getleftChild(self):
		if self.leftChild:
			return 2 + self.leftChild.getleftChild()
		else:
			return 1

	def getrightChild(self):
		if self.rightChild:
			return 1 + self.rightChild.getrightChild()
		else:
			return 1


	def find(self, key):
		if(self.key == key):
			return self.value
		elif self.key > key:
			if self.leftChild:
				return self.leftChild.find(key)
			else:
				return None
		else:
			if self.rightChild:
				return self.rightChild.find(key)
			else:
				return None



	def preorder(self):
		if self:
			print (str(self.value), end=' ')
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()

	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()
			print (str(self.value), end=' ')



	def inorder(self):
		if self:
			if self.leftChild:
				yield from self.leftChild.inorder()
			yield self.value

			if self.rightChild:
				yield from self.rightChild.inorder()





class Tree:
	def __init__(self):
		self.root = None

	def insert(self, key, data):
		if self.root:
			return self.root.insert(key, data)
		else:
			self.root = Node(key, data)
			return True

	def find(self, key):
		if self.root:
			return self.root.find(key)
		else:
			return False

	def _getHeight(self):
		if self.root:
			return self.root.getHeight()
		else:
			return 0

	def _getleftHeight(self):
		if self.root:
			return self.root.getleftChild()
		else:
			return 0

	def _getrightHeight(self):
		if self.root:
			return self.root.getrightChild()
		else:
			return 0


	def _minimum(self):
		current = self.root
		while current.leftChild != None:
			current = current.leftChild
		return current.value

	def _maximum(self):
		current = self.root
		while current.rightChild != None:
			current = current.rightChild
		return current.value



	def delete(self, data):

		#empty tree
		if self.root is None:
			return False

		#data is in root node
		elif self.root.value == data:
			if self.root.leftChild is None and self.root.rightChild is None:
				self.root = None
			elif self.root.leftChild and self.root.rightChild is None:
				self.root = self.root.leftChild
			elif self.root.leftChild is None and self.root.rightChild:
				self.root = self.root.rightChild
			elif self.root.leftChild and self.root.rightChild:
				delNodeParent = self.root
				delNode = self.root.rightChild
				while delNode.leftChild:
					delNodeParent = delNode
					delNode = delNode.leftChild

				self.root.value = delNode.value
				if delNode.rightChild:
					if delNodeParent.value > delNode.value:
						delNodeParent.leftChild = delNode.rightChild
					elif delNodeParent.value < delNode.value:
						delNodeParent.rightChild = delNode.rightChild

				else:
					if delNode.value < delNodeParent.value:
						delNodeParent.leftChild = None
					else:
						delNodeParent.rightChild = None

			return True

		parent = None
		node = self.root

		#find node to remove
		while node and node.value != data:
			parent = node
			if data < node.value:
				node = node.leftChild
			elif data > node.value:
				node = node.rightChild

		#case 1 : data not found
		if node is None or node.value != data:
			return False


		#case2 : remove-node has no children
		elif node.leftChild is None and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = None
			else:
				parent.rightChild = None
			return True

		#case3 : remove-node has left child only
		elif node.leftChild and node.rightChild is None:
			if data < parent.value:
				parent.leftChild = node.leftChild
			else:
				parent.rightChild = node.leftChild
			return True

		#case 4: remove-node has right child only
		elif node.leftChild is None and node.rightChild:
			if data < parent.value:
				parent.leftChild = node.rightChild
			else:
				parent.rightChild = node.rightChild
			return True

		#case 5: remove-node has left and right children
		else:
			delNodeParent = node
			delNode = node.rightChild
			while delNode.leftChild:
				delNodeParent = delNode
				delNode = delNode.leftChild

			node.value = delNode.value
			if delNode.rightChild:
				if delNodeParent.value > delNode.value:
					delNodeParent.leftChild = delNode.rightChild
				elif delNodeParent.value < delNode.value:
					delNodeParent.rightChild = delNode.rightChild
			else:
				if delNode.value < delNodeParent.value:
					delNodeParent.leftChild = None
				else:
					delNodeParent.rightChild = None


	def __getitem__(self, key):
		return self.find(key)

	def __setitem__(self, key, value):
		self.insert(key, value)

	def __contains__(self, key):
		if self[key]:
			return True
		else:
			return False
			

	def preorder(self):
		print("PreOrder")
		self.root.preorder()

	def postorder(self):
		print("PostOrder")
		self.root.postorder()

	def inorder(self):
		print("InOrder")
		return self.root.inorder()






if __name__ == "__main__":
	bst = Tree()
	bst._insert(10)
	bst._insert(3)
	bst._insert(4)
	bst._insert(13)
	bst._insert(15)
	bst._insert(1)
	bst._insert(11)

	print(" Tree looks like this \n")

	print("     10    " )
	print("  3     13  ")
	print("1  4  11  15\n")

	bst._preorder()
	print("\n")
	bst._postorder()
	print("\n")
	bst._inorder()
	print("\n")


	print("-----after removing number(1)-----\n")
	bst.delete(1)

	bst._preorder()
	print("\n")
	bst._postorder()
	print("\n")
	bst._inorder()
	print("\n")

	print("The height of tree is = ", bst._getHeight())

	print("\nThe left child height is = ", bst._getleftHeight())

	print("\nThe right child height is = ", bst._getrightHeight())


	

	print("\nThe maximum number is = ", bst._maximum())

	print("\nThe minimum number is = ", bst._minimum())


