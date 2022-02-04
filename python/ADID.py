import json


class Employee:
    Empid = int()
    Ename = ''
    Sal = int()
    Deptno = int()

    def Add_Emp():
        addemplist = {}
        # add employee
        try:
            Ename = input('Enter employee name: ')
            Ename = Ename.upper()
            addemplist['Employee_Name'] = Ename
        except:
            print('emp name error')

        Empid = int(input('Enter employee id: '))
        with open('empid.txt', 'r') as e:
            readfile = e.read()
            if str(Empid) in readfile:
                print('Empid must be unique')
                menu()
        e.close()
        if Empid < 999:
            print('emp id must be more than 3 characters')
            menu()
        else:
            addemplist['Employee_Id'] = Empid
            empid = str(Empid)
            with open('empid.txt', 'a') as f:
                f.write(empid)
                f.write('\n')
                f.close()

        try:
            Sal = int(input('Enter employee Salary: '))
            if Sal < 3000:
                print('Salary should be more than 3k')
            else:
                addemplist['Employee_Salary'] = Sal
        except:
            print('enter valid salary')
            menu()

        try:
            Deptno = int(input('Enter dept number: '))
            if(Deptno != 10 and Deptno != 20 and Deptno != 30):
                print('invalid dept number')
                menu()
            else:
                addemplist['Dept_No'] = Deptno
        except:
            print('enter valid dept number')
            menu()

        print('Employee added sucessfully...')
        file1 = open('emp.txt', 'a')
        file1.write(json.dumps(addemplist))
        file1.write('\n')
        file1.close()

    def Display_Emp():
        # display employee
        print('Displaying employee list')
        with open('emp.txt', 'r') as f:
            line = f.readline()
            cnt = 1
            while line:
                print("Employee {}: {}".format(cnt, line.strip()))
                line = f.readline()
                cnt += 1
           
    def Seperate_data():
        print('seperating data..')


def menu():
    while True:
        print('1.  Add_emp')
        print('2.  Display_emp')
        print('3.  Seperate_data')
        print('4.  Exit')
        userinput = int(input())
        if userinput == 1:
            Employee.Add_Emp()
        elif userinput == 2:
            Employee.Display_Emp()
        elif userinput == 3:
            Employee.Seperate_data()
        elif userinput == 4:
            quit()
        else:
            print('enter valid input')


menu()
