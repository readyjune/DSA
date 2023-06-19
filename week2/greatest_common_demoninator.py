#85 % 51 = 34
#51 % 34 = 17
#34 % 17 = 0
#17 % 0 = 


#--------


def gcd(x, y):
	if (x < 0 or y < 0):
		raise ValueError("it's a wrong number, number has to be more than 0")
	return gcd_rec(x, y)

def gcd_rec(x, y):
	if (y==0):
		return x
	else:
		return gcd_rec(y, x%y)

x = int(input("give me a first number ..."))
y = int(input("give me a second number ..."))

try:
	print(gcd(x, y))
except ValueError:
	print("Invalid number for input")
