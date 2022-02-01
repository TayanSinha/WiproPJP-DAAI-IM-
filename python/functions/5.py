def evennumbers(lst):
    for i in lst:
        if i%2 == 0:
            print(i, end = " ")
        else:
            continue
       
MyList1 = [1,2,8,4,5]
evennumbers(MyList1)