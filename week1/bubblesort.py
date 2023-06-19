import csv
import DSAsorts


#with open("RandomNames7000.csv") as file:
#	reader = csv.reader(file)
	
#f = open("RandomNames7000.csv", "r")
#data = f.read().split()
#f.close

#print(data, sep=",")

#	for j in range(len(reader)):
#		swapped = False
#		i = 0
#		while i < len(reader)-1:
#			if reader[i] > reader[i+1]:
#				reader[i], reader[i+1] = reader[i+1], reader[i]
#				swapped = True
#			i = i + 1
#		if swapped == False:
#			break


#def bubblesort(arr):
#	n = len(arr)
#
#	for i in range(n):
#		for j in range(0, n-i-1):
#			if arr[j] > arr[j+1]:
#				arr[j], arr[j+1] = arr[j+1], arr[j]

f = open("RandomNames7000.csv", "r")
data= f.read().splitlines()
f.close

DSAsorts.bubbleSort(data)


for i in range(len(data)):
	print(data[i], sep="\n")


