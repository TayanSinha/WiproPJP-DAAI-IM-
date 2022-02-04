
try:
	a= int(input('enter a number: '))
	flag = False
	if a > 1:
	    
	    for i in range(2, a):
	        if (a % i) == 0:
	            flag = True
	            break
	if flag:
	    print(a, "is not a prime number")
	else:
	    print(a, "is a prime number")
except:
	print('enter valid input')