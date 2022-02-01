str = input('Enter a string value: ')
if str[0] =='x' and str[-1] == 'x':
    print(str[1:(len(str))-1])
elif str[-1] == 'x':
    print(str[0:(len(str))-1])
elif str[0] == 'x':
  print(str[1:(len(str))])
else:
    print(str)