
with open('first.txt', 'r')  as f:
	content = f.readlines()                
	content = [x.strip() for x in content]




print(content)
