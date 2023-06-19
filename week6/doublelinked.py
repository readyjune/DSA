class Node:
	def __init__(self, data):
		self.item = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.start_node = None
		self.count = 0


	def __iter__(self):
		currNd = self.start_node
		while currNd is not None:
			yield currNd.item
			currNd = currNd.next

#	def __next__(self):
#		curval = None
#		if self.cur == None:
#			raise StopIteration
#		else:
#			curval = self.cur.item
#			self.cur = self.cur.next
#		return curval



	def is_empty(self):
		return self.count == 0


	def insert_in_emptylist(self, data):
		if self.is_empty() == True:
			new_node = Node(data)
			self.start_node = new_node
			self.count += 1
		else:
			print("list is not empty")
	def insert_to_end(self, data):
		if self.is_empty() == True:
			new_node = Node(data)
			self.start_node = new_node
			self.count += 1
			return
		n = self.start_node
		#iterate till thenext reaches NULL
		while n.next is not None:
			n = n.next
		new_node = Node(data)
		n.next = new_node
		new_node.prev = n
		self.count += 1

	def delete_at_start(self):
		if self.is_empty() == True:
			print("The Linked list is empty, no element to delete")
			return
		if self.start_node.next is None:
			self.start_node = None
			self.count -= 1
			return
		self.start_node = self.start_node.next
		self.start_prev = None
		self.count -= 1

	def delete_at_end(self):
		if self.is_empty() == True:
			print("The linked list is empty, no element to delete")
			return
		if self.start_node.next is None:
			self.start_node = None
			self.count -= 1
			return
		n = self.start_node
		while n.next is not None:
			n = n.next
		n.prev.next = None
		self.count -= 1

	def display(self):
		if self.is_empty() == True:
			print("The list is empty")
			return
		else:
			n = self.start_node
			while n is not None:
				print("Element is: ", n.item)
				n = n.next
			print("\n")


	def peekFirst(self):
		if self.is_empty() == True:
			print("The list is empty")
		else:
			return self.start_node.item


	def peekLast(self):
		n = self.start_node
		while n.next is not None:
			n = n.next
			continue
		return n.item

	def __str__(self):
		myString = ' '.join(str(item) for item in self)
		return myString

	def __contains__(self, value):
		for item in self:
			if item == value:
				return True
		return False

	def len(self):
		return self.count


if __name__ == "__main__":
	List = DoublyLinkedList()
	List.insert_in_emptylist(10)
	List.insert_to_end(20)
	List.insert_to_end(30)
	List.insert_to_end(40)
	List.insert_to_end(50)
	List.insert_to_end(60)
	List.insert_to_end(70)
	List.display()
	List.delete_at_start()
	List.display()
	List.delete_at_end()
	List.display()


	print(List.peekFirst())
	print(List.peekLast())




	myiter = iter(List)
	value = next(myiter)
	for value in List:
		print(value)
