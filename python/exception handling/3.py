try:
	alpha= input("enter file name:")
	with open(alpha,'r') as f:
		text= f.readlines()
		print(text)
except:
	print('file not found')