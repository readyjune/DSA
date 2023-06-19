#class DSAVector:
#	fields: vector_array (double array) count (int)
#	constant: DEFAULT_CAPACITY
#
#	default_constructor()
#		allocate array with DEFAULT_CAPACITY
#
#	get IMPORT index EXPORT item
#		item <- vector_array[index]
import numpy


class DSAVector:
	DEFAULT_CAPACITY = 3
	def __init__(self):
		self.capacity = DSAVector.DEFAULT_CAPACITY
		self.vector_array = numpy.zeros(DSAVector.DEFAULT_CAPACITY, dtype = float)
		self.count = 0

	def get(self, index):
		item = self.vector_array[index]
		return item

	def is_full(self):
		return self.count >= self.capacity

	def append(self, item):
		if self.is_full():
			new_array = numpy.zeros(self.capacity*2, dtype = float)
			for i in range(self.capacity):
				new_array[i] = self.vector_array[i]
			self.capacity *= 2
			self.vector_array = new_array

		self.vector_array[self.count] = item
		self.count += 1

if __name__ == "__main__":
	test_vector = DSAVector()
	test_vector.append(20)
	test_vector.append(350)
	test_vector.append(350)
	test_vector.append(350)
	test_vector.append(350)
	test_vector.append(350)
	for i in range(test_vector.count):
		print(test_vector.get(i))	
