n = int(input("enter a number \n"))
sum = 0
while (n != 0):
    sum = sum + (n % 10)
    n = n//10
print(sum)
       