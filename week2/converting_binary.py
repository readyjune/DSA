

####------


def convert(n):
	if (n<1):
		raise ValueError("You gave me a wrong number")
	convert_rec(n)
	print()

def convert_rec(n):
	if (n>1):
		convert_rec(n//2)
	print(n % 2, end = '')

n = int(input("give me a number..."))

try:
	convert(n)
except ValueError:
	print("Invalid number for input")
