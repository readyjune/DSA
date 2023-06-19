import numpy

class Stack:
	capacity = 100
	def __init__(self):
		self.capacity = Stack.capacity
		self.stack_array = numpy.zeros(Stack.capacity, dtype = object)
		self.count = 0

	def len(self):
		return self.count

	def is_empty(self):
		return self.count == 0

	def is_full(self):
		return self.count >= self.capacity

	def append(self, item):
		if self.is_full() == True:
			raise IndexError("Stack is full")
		else:
			self.stack_array[self.count] = item
			self.count += 1
	
	def peek(self):
		return self.stack_array[self.count-1]


	def pop(self):
		if self.is_empty() == True:
			print('stack is empty')
		else:
			if len(self.stack_array) <  1:
				raise ValueError('stack is empty')
			top = self.stack_array[self.count-1]
			self.count -= 1
			return top

	def __str__(self):
		myString = ' '.join(str(self.stack_array[i]) for i in range(self.count))
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
