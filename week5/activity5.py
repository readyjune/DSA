from BinarySearchTree import *
import csv
from csv import writer
import pickle

print("1. read a CSV file")
print("2. read a serialized file")
print("3. display the tree")
print("4. write a CSV file")
print("5. write a serialized file")
print("6. EXIT")

choice = input("choose the number : 1, 2, 3, 4, 5, 6....... ")
#csv.reader(f)

b=Tree()

while choice[0] != '6':
	if choice[0] == '1':
		print("read a CSV file")
		with open("numbers.csv", "r") as f:
			abc = [line.strip() for line in f]
			print([int(x) for x in abc])
		f.close()


	elif choice[0] == '2':
		print("read a serialized file")
		with open("numbers.rob", "rb") as f:
			data = pickle.load(f)
			print(data)
			with open("numbers.csv", "r") as f:
				reader = csv.reader(f)
				for i in reader:
					print(i, end=' ')


			f.close()

	elif choice[0] == '3':
		print("display the tree")
		print("hahaha this part is hard...")


	elif choice[0] == '4':
		print("write a CSV file")
		print("1. inorder  2. preorder  3. postorder")
		selection = input("choose the number you want to see")
		
		with open("numbers.csv", "r") as f:
			abc = [line.strip() for line in f]
			hello = [int(x) for x in abc]
			for i in range(len(hello)):
				b._insert(hello[i])	


	
#			b._insert(hello[0])
#			b._insert(hello[1])
#			b._insert(hello[2])
#			b._insert(hello[3])
#			b._insert(hello[4])
#			b._insert(hello[5])
#			b._insert(hello[6])
	
		if selection == "1":
			b._inorder()
		elif selection == "2":
			b._preorder()
		else:
			b._postorder			
			

		#choice = input("which number do you want to put : ")
		#a = [choice]
		#with open("numbers.csv", "a") as f:
		#	f_object  = writer(f)
		#	f_object.writerow(a)
		#	f.close()

	elif choice[0] == '5':
		print("write a serialized file")
		with open("numbers.rob", "wb") as f:
			pickle.dump("numbers.csv", f)

	choice = input("\n\n\n\n\nchoose the number : 1, 2, 3, 4, 5, 6....... \n")



print("Goodbye\n")
