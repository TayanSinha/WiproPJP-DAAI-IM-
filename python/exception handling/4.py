
list1=[1,-2,10,-32,23,76,88,-93,34,67]
try:
	a= int(input('enter a index: '))
	if list1[a]>0:
		print('it is a positive number')
	else:
		print('it is a negative number ')
except:
	print('enter valid input')