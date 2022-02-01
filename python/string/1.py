str = "Alpha Joined our TEam"
count1 = 0
count2 = 0
for i in str:
    if i.islower():
        count1= count1+1
    elif(i.isupper()):
        count2=count2+1
print('total number of lower char is :', count1)
print('total number of upper char is :', count2)