import numpy

class Queue:
	capacity = 100
	def __init__(self):
		self.capacity = Queue.capacity
		self.queue_array = numpy.zeros(Queue.capacity, dtype = object)
		self.count = 0

	def len(self):
		return self.count

	def is_empty(self):
		return self.count == 0

	def is_full(self):
		return self.count >= self.capacity

	def append(self, item):
		if self.is_full() == True:
			raise IndexError("Queue is full")
		else:
			self.queue_array[self.count] = item
			self.count += 1

	def peek(self):
		return self.stack_array[self.count-1]

	def pop(self):
		if self.is_empty() == True:
			print("Stack is empty")
		else:
			if len(self.queue_array) < 1:
				raise ValueError("Stack is empty!!!")
			bottom = self.queue_array[0]
			for i in range(self.count):
				self.queue_array[i] = self.queue_array[i+1]
			self.count -= 1
			return bottom


	def __str__(self):
		myString = ' '.join(str(self.queue_array[i]) for i in range(self.count))
		return myString


#	def pop(self):
#		if self.is_empty():
#			print('stack is empty')
#		else:
#			if len(self.data) == 1:
#				print('stack is empty')
#			return self.data.pop(0)





if __name__ == "__main__":
	test_queue = Queue()
	test_queue.append(1)
	print(test_queue)

	test_queue.append(2)
	print(test_queue)

	test_queue.append(3)
	print(test_queue)

	test_queue.append(4)
	print(test_queue)

	test_queue.pop()
	print(test_queue)

	test_queue.pop()
	print(test_queue)


	test_queue.pop()
	print(test_queue)

	test_queue.pop()
	print(test_queue)
