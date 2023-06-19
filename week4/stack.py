from doublelinked import DoublyLinkedList


class Stack:
	capacity = 100
	def __init__(self):
		self.capacity = Stack.capacity
		self.stack_list = DoublyLinkedList()

	def len(self):
		return self.stack_list.count

	def is_empty(self):
		return self.stack_list.count == 0

	def is_full(self):
		return self.stack_list.count >= self.capacity

	def append(self, item):
		if self.is_full() == True:
			raise IndexError("Stack is full")
		else:
			self.stack_list.insert_to_end(item)

	
	def peek(self):
		return self.stack_list.peekFirst()


	def pop(self):
		if self.is_empty() == True:
			print('stack is empty')
		else:
			item = self.stack_list.peekLast()
			self.stack_list.delete_at_end()
			return item			


	def __str__(self):
		myString = ' '.join(str(item) for item in self.stack_list)
		return myString


if __name__ == "__main__":
	test_stack = Stack()
	test_stack.append(1)
	print(test_stack)

	test_stack.append(2)
	print(test_stack)

	test_stack.append(3)
	print(test_stack)

	test_stack.append(4)
	print(test_stack)

	test_stack.pop()
	print(test_stack)

	test_stack.pop()
	print(test_stack)


	test_stack.pop()
	print(test_stack)

	test_stack.pop()
	print(test_stack)
