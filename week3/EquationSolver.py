from stack_array_but_problem import Stack
a = '3+5*2/(7-2)'
res = ''
stack = Stack()
for x in a:
	if x.isdecimal():
		res += str(x)
	else:
		if x == '(':
			stack.append(x)
		elif x == '*' or x == '/':
			while not stack.is_empty() and (stack.peek() == '*' or stack.peek() == '/'):
				print(f"the stack is {stack} and x is {x}")
				res += stack.pop()
			stack.append(x)

		elif x == '+' or x == '-':
			while not stack.is_empty() and stack.peek() != '(':
				print(f"the stack is {stack} and x is {x}")
				res += stack.pop()
			stack.append(x)
		elif x == ')':
			while stack and stack.peek() != '(':
				res += stack.pop()
			stack.pop()


while not stack.is_empty():
	res += stack.pop()

print(res)







#def solve(equation):


#def _parselnfixToPostfix(equation):


#def _evaluatePostfix(postfixQueue):


#def _precedenceOf(theOp):


#def _excuteOperation(op, op1, op2)
