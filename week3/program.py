from vector import DSAVector



numbers = DSAVector()
more_numbers = DSAVector()

numbers.append(23)
more_numbers.append(500)

print(numbers.get(0))
print(f"the more numbers vector has {more_numbers.count} numbers in ")
print(f"It's first number is {more_numbers.get(0)}")
