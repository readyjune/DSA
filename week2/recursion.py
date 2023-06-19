def _count_down_rec(n):
	if n == 0:
		return
	print(n)
	_count_down_rec(n-1)


def count_down(n):
	if n < 0:
		raise ValueError("This function does not work with negative numbers")
	_count_down_rec(n)

count_down(-100)


