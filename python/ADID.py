import json
import os
from sys import argv


# defining a Employee class with empid,ename,sal and depno variable
class Employee:
    Empid = int()
    Ename = ''
    Sal = int()
    Deptno = int()

# *add employee* method for adding employee
    def Add_Emp():
        addemplist = {}
        try:
            Ename = input('Enter employee name: ')
        # uppercasing entered name
            Ename = Ename.upper()
            addemplist['Employee_Name'] = Ename
        except:
            print('error while entering employee name')
        Empid = int(input('Enter employee id: '))
        # checking employee id is unique or not
        try:
            with open('empid.txt', 'x') as e:
                readfile= e.read()
        except:
            with open('empid.txt', 'r') as e:
                readfile = e.read()
        if str(Empid) in readfile:
            print('Empid must be unique\n')
            menu()
        e.close()
        # checking employee id is more than 3 characters or not
        if Empid < 999:
            print('emp id must be more than 3 characters\n')
            menu()
        else:
            addemplist['Employee_Id'] = Empid
            empid = str(Empid)
            try:
                open('empid.txt', 'x')
            except:
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
            print('enter valid salary\n')
            menu()

        try:
            Deptno = int(input('Enter dept number: '))
            if(Deptno != 10 and Deptno != 20 and Deptno != 30):
                # checking if dep id is in-between 10,20 and 30
                print('invalid dept number\n')
                menu()
            else:
                addemplist['Dept_No'] = Deptno
        except:
            print('enter valid dept number\n')
            menu()

        print('Employee added sucessfully...')
        # adding employee details to local txt file namely emp.txt
        try:
            file1=open('emp.txt', 'x')
            file1.write(json.dumps(addemplist))
            file1.write('\n')
            file1.close()
        except:
            file1 = open('emp.txt', 'a')
            file1.write(json.dumps(addemplist))
            file1.write('\n')
            file1.close()

# display employee
    def Display_Emp():
        print('Displaying employee list:')
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
        print('Seperating data...\n.\n.\n.')
        with open('emp.txt', 'r') as f:
            content_list = [line.rstrip('\n') for line in f]
            f.close()
        # checking if emp_dep files do exist & if exist then deleting the old files and creating new to store value freshly
        if os.path.exists("emp_10.txt"):
            os.remove("emp_10.txt")
        if os.path.exists("emp_20.txt"):
            os.remove("emp_20.txt")
        if os.path.exists("emp_30.txt"):
            os.remove("emp_30.txt")
        open('emp_10.txt', 'x')
        open('emp_20.txt', 'x')
        open('emp_30.txt', 'x')

        # accessing the employee data from emp.txt and seperating them according to their dep number
        line = ''
        for i in range(len(content_list)):
            line = content_list[i]
            if (line[-3:len(line)-1]) == '10':
                with open('emp_10.txt', 'a') as s:
                    l = s.write(line+'\n')
            elif (line[-3:len(line)-1]) == '20':
                with open('emp_20.txt', 'a') as s:
                    l = s.write(line+'\n')
            elif (line[-3:len(line)-1]) == '30':
                with open('emp_30.txt', 'a') as s:
                    l = s.write(line+'\n')
        print("Data Seperated Sucessfully\n")

# adding menu driven feature to our program


def menu():
    while True:
        print(' EMPLOYEE MANAGEMENT ')
        print('1.  Add_emp')
        print('2.  Display_emp')
        print('3.  Seperate_data')
        print('4.  Exit')
        userinput = int(input('Enter your choice:\t'))
        if userinput == 1:
            Employee.Add_Emp()
        elif userinput == 2:
            Employee.Display_Emp()
        elif userinput == 3:
            Employee.Seperate_data()
        elif userinput == 4:
            quit()
        else:
            print('enter valid input\n')

# main function


# adding command line argument feature
try:
    s = argv[1]
    if s == '1':
        Employee.Add_Emp()
    elif s == '2':
        Employee.Display_Emp()
    elif s == '3':
        Employee.Seperate_data()
    else:
        print('nota a valid command line input, try again')
except:
    menu()
