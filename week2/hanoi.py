def hanoi(n, start, end, helper):
	if n == 1:
		print("Moving top disk from peg source", start, "to peg destination", end)
		return

	hanoi(n - 1, start, helper, end)

	print("Moving top disk from peg source", start, "to peg destination", end)

	hanoi(n - 1, helper, end, start)



p = int(input("how many disk do you want?"))





print(' n = ', p)
hanoi(p, "A", "B", "C")


print("\n")






#------------------
#hanoi(3, 1, 3, 2)
#	hanoi(2, 1, 2, 3)
#		hanoi(1, 1, 3, 2)
#		hanoi(1, 3, 2, 1)
#	hanoi(2, 2, 3, 1)
#		hanoi(1, 2, 1, 3)
#		hanoi(1, 1, 3, 2)



