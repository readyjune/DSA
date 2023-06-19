#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

#A =  [1, 3, 5, 7, 8, 2, 4]

def bubbleSort(A):
	for j in range(len(A)):
		swapped = False
		i = 0
		while i<len(A)-1:
			if A[i]>A[i+1]:
				A[i], A[i+1] = A[i+1], A[i]
				swapped = True
			i = i + 1
		if swapped == False:
			break

#bubbleSort(A)
#print(A)



#B = [5, 4, 2, 1, 3]

def insertionSort(A):
	for i in range(1, len(A)):
		key_item = A[i]
		j = i - 1
		while j >= 0 and A[j] > key_item:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key_item
	return A

#insertionSort(B)
#print(B)



#C = [7, 3, 5, 2, 1]


def selectionSort(A):

	for i in range(len(A)):
		minimum = i
		for j in range(i+1, len(A)):
			if A[minimum] > A[j]:
				minimum	= j
		A[i], A[minimum] = A[minimum], A[i]

#selectionSort(C)
#print(C)
