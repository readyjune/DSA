import pickle

def bucket():
	print('\nBUCKET LIST BUILDER\n')

	bucket = []

	choice = input('Enter selection: e(X)it, (A)dd, (L)ist, (D)elete...')

	choice = choice.upper()

	while choice[0] != 'X':
		if choice[0] == 'A':
			print('Enter list item... ')
			newitem = input()
			bucket.append(newitem)
		elif choice[0] == 'L':
			for item in bucket:
				print(item)
		elif choice[0] == 'D':        
			print('Delete item number... ')
			delitem = input()
			del bucket[int(delitem)-1]
			for item in bucket:
				print('The rest of item is', item)
        
		else:
			print('Invalid selection.')
		choice = input('Enter selection: e(X)it, (A)dd, (L)ist, (D)elete...')
		choice = choice.upper()

	print('\nGOODBYE!\n')


#searalized

with open("activity5.rob", "wb") as output_activity5:
	pickle.dump(bucket, output_activity5)
