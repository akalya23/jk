def poweroftwo(x):
	return (x and (not(x & (x - 1))))
n1 = int(input())
if(poweroftwo(n)):
	print("yes")
else:
	print("no")
