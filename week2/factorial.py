
def calc(n):
	if (n<0):
		raise ValueError("the number should be more than 0")
	return calc_rec(n)


def calc_rec(n):
	factorail =1 
	if (n==0):
		factorial = 1
	else:
		factorial = n * calc_rec(n-1)
	return factorial

a = int(input("give me a number ... "))

#print(calc(a))

try:
	print(calc(a))
except ValueError:
	print("Invalid number for input")


