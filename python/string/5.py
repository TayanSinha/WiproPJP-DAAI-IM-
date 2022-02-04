str = input('Enter a string value: ')
int1 = int(input('Enter a int value: '))
strlen= len(str)
if (int1 == 0) or (int1 > strlen):
    print('int length should be more than 0 char and less than string length')
    quit()
else:
    str2=str [len(str)-int1:len(str)]
    for i in range(int1):
        print(str2, end = "")