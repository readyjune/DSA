import numpy

class CircularQueue:
	capacity = 5
	def __init__(self):
		self.capacity = CircularQueue.capacity
		self.queue = numpy.zeros(CircularQueue.capacity, dtype = object)
		self.front = self.rear = -1
		self.count = 0


	def len(self):
		return self.count % self.capacity

	def isEmpty(self):
		return self.front == -1

	def isFull(self):
		return ((self.rear + 1) %  self.capacity == self.front)

	def Enqueue(self, item):
		if self.isFull() == True:
			raise IndexError('Queue is full')
		elif self.front == -1:
			self.front = 0
			self.rear = 0
			self.queue[self.rear] = item
			self.count += 1
		else:
			self.rear = (self.rear + 1) % self.capacity
			self.queue[self.rear] = item
			self.count += 1

	def Dequeue(self):
		if (self.isEmpty()) == True:
			print("Queue is empty")
		elif self.front == self.rear:
			temp = self.queue[self.front]
			self.front = -1 
			self.rear = -1
			self.count -= 1
			return temp

		else:
			bottom = self.queue[self.front]
			#No need to loop, just move the "front" up by one
			self.front += 1 % self.capacity
			self.count -= 1

			return bottom




	def __str__(self):
		#loop from the "front" to the "end"
		myString = ' '.join(str(self.queue[(self.front + i) % self.capacity]) for i in range(self.count))
		return myString


if __name__ == "__main__":
	a = CircularQueue()
	a.Enqueue(1)
	print(a.queue)
	print(a)
	a.Enqueue(2)
	print(a.queue)
	print(a)
	a.Enqueue(3)
	print(a.queue)
	print(a)
	a.Enqueue(4)
	print(a.queue)
	print(a)
	a.Dequeue()	
	print(a.queue)
	print(a)
	a.Dequeue()
	print(a.queue)
	print(a)
	a.Enqueue(5)
	print(a.queue)
	print(a)
	a.Dequeue()
	print(a.queue)
	print(a)
	a.Dequeue()
	print(a.queue)
	print(a)
	a.Enqueue(6)
	print(a.queue)
	print(a)

