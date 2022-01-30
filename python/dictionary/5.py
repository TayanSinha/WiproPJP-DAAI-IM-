k=0
Mydict3={}
for k in range(1,15): 
    Mydict2 = {k:k*k}
    Mydict3 = Mydict3 | Mydict2
print(Mydict3)