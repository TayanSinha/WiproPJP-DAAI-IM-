with open('a.txt') as f:
    lines = f.readlines()
linenum=int(input('enter number of lines you want to read: '))
count =0
linen=[]
for line in lines:
	linen.append(line)
	count+=1
	
for i in range(len(linen)):
	print(linen[i])