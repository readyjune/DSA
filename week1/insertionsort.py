import csv

def insertionSort(A):
	for i in range(1, len(A)):
		key_item = A[i]
		j = i - 1
		while j >= 0 and A[j] > key_item:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key_item
	return A

f = open("RandomNames7000.csv", "r")
data = f.read().splitlines()
f.close()


insertionSort(data)


for i in range(len(data)):
	print(data[i], sep="\n")
