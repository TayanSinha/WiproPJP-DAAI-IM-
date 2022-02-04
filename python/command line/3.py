import  sys
b=int(0)
for i in range(10):
	a=int(sys.argv[i+1])
	b=b+a
print(b)