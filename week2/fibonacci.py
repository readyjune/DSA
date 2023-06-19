def fibRecursive(n):
	if (n < 0):
		raise ValueError("the nuber should be more than 0")
	return fibRecursive_rec(n)



def fibRecursive_rec(n):
	fibVal = 0
	if (n==0):
		fibVal = 0
	elif (n==1):
		fibVal = 1
	else:
		fibVal = fibRecursive_rec(n-1) + fibRecursive_rec(n-2)
	return fibVal


n = int(input("give me a number..."))



#print(fibRecursive(n))

try:
	print(fibRecursive(n))
except ValueError:
	print("Invalid number for input")
	
