rows = 10
cols = 5
while True:
	for i in range(rows):
		print('*' + ('*' if i in (0,rows-1) else ' ') * (cols-2)+ '*')
	break	