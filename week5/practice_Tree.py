class Node:
	def __init__(self, val):
		self.val = val
		self.leftChild = None
		self.rightChild = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

	def setRoot(self, val):
		self.root = Node(val)

	def find(self, val):
		if (self.findNode(self.root, val) is False):
			return False
		else:
			return True

	def findNode(self, currentNode, val):
		if (currentNode is None):
			return False
		elif (val == currentNode.val):
			return currentNode
		elif (val < currentNode.val):
			return self.findNode(currentNode.leftChild, val)
		else:
			return self.findNode(currentNode.rightChild, val)

	def insert(self, val):
		if (self.root is None):
			self.setRoot(val)
		else:
			self.insertNode(self.root, val)

	def insertNode(self, currentNode, val):
		if (val <= currentNode.val):
			if (currentNode.leftChild):
				self.insertNode(currentNode.leftChild, val)
			else:
				currentNode.leftChild = Node(val)
		elif (val > currentNode.val):
			if (currentNode.rightChild):
				self.insertNode(currentNode.rightChild, val)
			else:
				currentNode.rightChild = Node(val)


	def delete(self, val):
		if self == None:
			return self
		else:
			self.deleteNode(self.root, val)

	def deleteNode(self, currentNode, val):
		if val < currentNode.val:
			currentNode.leftChild = self.deleteNode(currentNode.leftChild, val)
		elif val > currentNode.val:
			currentNode.rightChild = self.deleteNode(currentNode.rightChild, val)
		else:
			# case 1 : node is a leaf node
			if currentNode.leftchild == none and currentNode.rightchild == none:
				currentNode = none

			# case 2 : node has only one child
			elif currentNode.leftchild == none:
				temp = currentNode
				currentNode = currentNode.rightchild

			elif currentNode.rightchild == none:
				temp = currentNode
				currentNode = currentNode.leftchild

			# case 3 : has both children
			else:
				temp = minimum(currentNode.rightchild)
				currentNode.val = temp.val
				currentNode.rightchild = self.deleteNode(currentNode.rightchild, temp.val)
		return currentNode
			




	def minimun(self, currentNode):
		while currentNode.leftchild != none:
			currentNode = currentNode.leftchild
		return currentNode

	def maximum(self, currentNode):
		while currentNode.rightchild != none:
			currentNode = currentNode.rightchild
		return currentNode


	def traverse(self):
		return self.traverseNode(self.root)

	def traversenode(self, currentNode):
		result = []
		if (currentNode.leftchild is not none):
			result.extend(self.traverseNode(currentNode.leftchild))
		if (currentNode is not none):
			result.extend([currentNode.val])
		if (currentNode.rightchild is not none):
			result.extend(self.traverseNode(currentNode.rightchild))
		return result



	def preorder(self, currentNode):
		return = []
		if currentNode.leftChild != None:
			result.extend(self.preorder(currentNode.leftChild))

		if currentNode.rightChild != None:
			result.extend(self.preorder.preorder(currentNode.rightChild))
		return result

if __name__ ==  "__main__":
	a = BinarySearchTree()
	a.setRoot()
	print(a)
