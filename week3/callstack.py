from stack import Stack


a = Stack()

def fibo(n):
	if n <= 1:
		return n
	else:
		return(fibo(n-1) + fibo(n-2))

nterms = 10

if nterms <= 0:
	print("please put positive number")
else:
	print("Fibonacci sequence:")
	for i in range(nterms):
		a.append(fibo(i))
	print(a)



##################################################

#a.append(1)
#a.append(2)
#a.append(3)
#a.append(4)
#a.pop()
#a.append(5)
#print(f"Stack function has {a}")
#b = fibo(5)

#print(b)


