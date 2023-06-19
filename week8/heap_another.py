class MaxHeap:
	def __init__(self, data):
		self.heap_array = list()
		self.heap_array.append(None)
		self.heap_array.append(data)

	def insertHeap(self, data):
		if len(self.heap_array) == 0:
			self.heap_array.append(None)
			self.heap_array.append(data)
			return False

		self.heap_array.append(data)
		newNode_idx = len(self.heap_array) - 1

		while self.compareNode_insert(newNode_idx):
			parentNode_idx = newNode_idx // 2
			self.heap_array[newNode_idx], self.heap_array[parentNode_idx] = self.heap_array[parentNode_idx], self.heap_array[newNode_idx]
			newNode_idx = parentNode_idx

		return True

	def compareNode_insert(self, newNode_idx):
		if newNode_idx <= 1:
			return False

		parentNode_idx = newNode_idx // 2

		if self.heap_array[newNode_idx] > self.heap_array[parentNode_idx]:
			return True
		else:
			return False


	def deleteHeap(self):
		if len(self.heap_array) <= 1:
			return None

		return_data = self.heap_array[1]
		temp_data = self.heap_array[-1]
		self.heap_array[1] = self.heap_array[-1]
		del self.heap_array[-1]
		parent_idx = 1
		child_idx = 2

		while (child_idx <= len(self.heap_array)):
			if child_idx + 1 >= len(self.heap_array):
				if self.heap_array[parent_idx] < self.heap_array[child_idx]:
					self.heap_array[child_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[child_idx]
				else:
					break
			elif self.heap_array[child_idx] >= self.heap_array[child_idx + 1]:
				if self.heap_array[child_idx] > self.heap_array[parent_idx]:
					self.heap_array[child_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[child_idx]
				else:
					break

			else:
				if self.heap_array[child_idx + 1] > self.heap_array[parent_idx]:
					self.heap_array[child_idx + 1], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[child_idx + 1]
				else:
					break

			parent_idx = parent_idx * 1
			child_idx = child_idx * 2

		return return_data

	def readHeap(self):
		for index in range(len(self.heap_array)-1):
			print(self.heap_array[index + 1])


if __name__ == "__main__":
	A = MaxHeap(15)
	A.insertHeap(20)
	A.insertHeap(29)
	A.insertHeap(16)
	A.insertHeap(3)
	A.insertHeap(36)

	A.readHeap()

	print("Most largest heap value will be deleted")
	delete_value = A.deleteHeap()
	print(delete_value)

	print("After deleting, now the heap has:")
	A.readHeap()
