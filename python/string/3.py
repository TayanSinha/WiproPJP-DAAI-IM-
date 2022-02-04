str = input('Enter a string value')

if (len(str))<=2:
    print('string length should be more than 2 char')
    quit()
else:
    str2=str[0:2]
    for i in range(len(str)):
        print(str2, end = "")