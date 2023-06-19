from doublelinked import DoublyLinkedList
import numpy as np




class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __str__(self):
		myString = f'key:  {self.key}   value : {self.value}'
		return myString


class HashTable:
	def __init__(self, size):
		self.table = np.empty(size, dtype=object)
		#self.table = [None] * size
		self.size = size
		self.count = 0
		self.is_resizing = False

	def loadfactor(self):
		return	self.count / self.size

	def resize(self):
		self.is_resizing = True
		self.size *= 2
		old_table = self.table

		new_table = np.empty(self.size, dtype = object)
		


		self.table = new_table
		for i in range(0, len(old_table)):
			if old_table[i]:
				for j in old_table[i]: 
					self.add( j.key, j.value )
		self.is_resizing = False


	def hashKey(self, key):
		hashString = 0
		for character in str(key):
			hashString += ord(character)
		return hashString % self.size

	def add(self, key, value):
		if self.loadfactor() > 0.5:
			self.resize()









		idx = self.hashKey(key)
	#	key_value = [key, value]
		if self.table[idx] is None:
			newLinkedList = DoublyLinkedList()
			newLinkedList.insert_to_end(Node(key, value))
		#	newLinkedList.insert_to_end(key)
		#	newLinkedList.insert_to_end(value)
			self.table[idx] = newLinkedList
			if not self.is_resizing:
				self.count += 1
		else:
			self.table[idx].insert_to_end(Node(key, value))
			if not self.is_resizing:
				self.count += 1
		#	self.table[idx].insert_to_end(key)
		#	self.table[idx].insert_to_end(value)

	def get(self, key):
		idx = self.hashKey(key)
		if self.table[idx] is not None:
			for pair in self.table[idx]:
				if pair.key == key:
					return pair.value
		return None			


	def printAll(self):
		print('----PHONEBOOK----')
		for i in self.table:
			if i is not None:
				i.display()

	def allkeys(self):
		A = DoublyLinkedList()
		for i in range(0, len(self.table)):
			if self.table[i]:
				B = DoublyLinkedList()
				for j in self.table[i]: 
					B.insert_to_end( j.key )
				A.insert_to_end(B)
		return A



	def delete(self, key):
		idx = self.hashKey(key)
		if self.table[idx] is None:
			return False

		if self.table[idx] is not None:
			for pair in self.table[idx]:
				if pair.key == key:
					self.table[idx].delete_element_by_value(pair)
					self.count -= 1

					if self.table[idx].is_empty():
						self.table[idx] = None


		#if self.table[idx].peekFirst()[0] == key:
		#	self.table[idx].delete_element_by_value(Node(key, value))
		#	self.table[idx].delete_at_end()
		#	self.table[idx].delete_at_end()
		#	return True

	def keys(self):
		A = DoublyLinkedList()
		for i in range(0, len(self.table)):
			if self.table[i]:
				for j in self.table[i]: 
					A.insert_to_end( j.key )
		return A

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		self.add(key, value)




if __name__ == "__main__":
	h = HashTable(8)
	h.add('A', '111-1111')
	h.add('B', '222-2222')
	h.add('C', '333-3333')
	h.add('D', '444-4444')
	h.add('E', '555-5555')
	h.add('F', '666-6666')
	h.add('G', '777-7777')
	h.add('H', '888-8888')
	h['I'] = '999-9999'


	print("What is in the C value")
	print(h['C'])

	h.printAll()
	print("after deleteing B")
	h.delete('B')
	h.printAll()
	print("what is in the key")
	print(h.keys())

	print("what is the value of the key 'A'...?\n")
	print(h.get('A'))

	print("What is in the value in this key")
	for collision in h.allkeys():
		print(collision)

	print("how many key do you have")
	print(h.count)
