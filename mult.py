def print3(x):
	print(x,' ',end='')
	if x <= 9:
		print(' ',end='')
	
	
def foo(start, end):
	for i in range(start,end+1,1):
		for j in range(start,end+1,1):
			print3(i* j)
		print("")

foo(1,9)

