import json
import os


class Employee:
    Empid = int()
    Ename = ''
    Sal = int()
    Deptno = int()

# add employee
    def Add_Emp():
        addemplist = {}
        try:
            Ename = input('Enter employee name: ')
            # uppercasing entered name
            Ename = Ename.upper()
            addemplist['Employee_Name'] = Ename
        except:
            print('emp name error')

        Empid = int(input('Enter employee id: '))
        # checking employee id is unique or not
        with open('empid.txt', 'r') as e:
            readfile = e.read()
            if str(Empid) in readfile:
                print('Empid must be unique')
                menu()
        e.close()
        # checking employee id is more than 3 characters or not
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
            # checking if salary is more than 3k or not
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
                # checking if dep id is in-between 10,20 and 30
                print('invalid dept number')
                menu()
            else:
                addemplist['Dept_No'] = Deptno
        except:
            print('enter valid dept number')
            menu()

        print('Employee added sucessfully...')
        # adding employee details to local txt file namely emp.txt
        file1 = open('emp.txt', 'a')
        file1.write(json.dumps(addemplist))
        file1.write('\n')
        file1.close()

# display employee
    def Display_Emp():
        print('Displaying employee list')
        with open('emp.txt', 'r') as f:
            line = f.readline()
            cnt = 1
            # displaying employee detail line by line
            while line:
                print("Employee {}: {}".format(cnt, line.strip()))
                line = f.readline()
                cnt += 1

# seperate data
    def Seperate_data():
        print('seperating data..')
        with open('emp.txt', 'r') as f:
            content_list = [line.rstrip('\n') for line in f]
            f.close()
            print(len(content_list))
        if os.path.exists("emp_10.txt"):
            os.remove("emp_10.txt")
        if os.path.exists("emp_20.txt"):
            os.remove("emp_20.txt")
        if os.path.exists("emp_30.txt"):
            os.remove("emp_30.txt")
        open('emp_10.txt', 'x')
        open('emp_20.txt', 'x')
        open('emp_30.txt', 'x')

        line = ''
        for i in range(len(content_list)):
            line = content_list[i]
            if (line[-3:len(line)-1]) == '10':
                with open('emp_10.txt', 'a') as s:
                    l = s.write(line)

            elif (line[-3:len(line)-1]) == '20':
                with open('emp_20.txt', 'a') as s:
                    l = s.write(line)

            elif (line[-3:len(line)-1]) == '30':
                with open('emp_30.txt', 'a') as s:
                    l = s.write(line)


# adding menu driven feature to our program
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


# main function
menu()
