def say_hi_x_times(x):
	print_x_times(x, "hi")



def print_x_times(x, text):
	if x <= 0:
		raise ValueError("something went wrong!!!")
	_print_x_times_rec(x, text)



def _print_x_times_rec(x, text):
	print(text)
	if x > 1:
		_print_x_times_rec(x-1, text)



text = input("what would you like to say?")
x = int(input("how many times would it be repeated?"))

try:
	print_x_times(x, text)
except ValueError:
	print("Invalid number of times!")

