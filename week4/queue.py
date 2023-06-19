from doublelinked import DoublyLinkedList 

class Queue:
	capacity = 100
	def __init__(self):
		self.capacity = Queue.capacity
		self.queue_list = DoublyLinkedList()

	def len(self):
		return self.queue_list.count

	def is_empty(self):
		return self.queue_list.count == 0


	def append(self, item):
		self.queue_list.insert_to_end(item)

	def peek(self):
		return self.queue_list.peekFirst()

	def pop(self):
		if self.is_empty() == True:
			print("queue is empty")
		else:

			item = self.queue_list.peekFirst()
			self.queue_list.delete_at_start()
			return item


	def __str__(self):
		myString = ' '.join(str(item) for item in self.queue_list)
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
	test_queue.queue_list.display()

	test_queue.pop()
	print(test_queue)

	test_queue.pop()
	print(test_queue)


	test_queue.pop()
	print(test_queue)

	test_queue.pop()
	print(test_queue)
