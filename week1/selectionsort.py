import csv

def selectionSort(A):

	for i in range(len(A)):
		minimum = i
		for j in range(i+1, len(A)):
			if A[minimum] > A[j]:
				minimum	= j
		A[i], A[minimum] = A[minimum], A[i]

f = open("RandomNames7000.csv", "r")
data = f.read().splitlines()
f.close()

selectionSort(data)

for i in range(len(data)):
	print(data[i], sep="\n")
