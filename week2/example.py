x = 10
y = 0


try:
	answer = x/y
except ZeroDivisionError as e:
	print("Something Went Wrong! %s!" % str(e))
finally:
	answer = 0
print(answer)


