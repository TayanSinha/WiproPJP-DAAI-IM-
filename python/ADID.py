import json
class Employee:
	Empid=int()
	Ename =''
	Sal=int()
	Deptno=int()
	
	def Add_Emp():
		addemplist={}
		#add employee
		try:
			Ename = input('Enter employee name: ')
			Ename= Ename.upper()
			addemplist['Employee_Name']=Ename
		except:
			print('emp name error')
		
		
		Empid= int(input('Enter employee id: '))
		with open('empid.txt','r') as e:
			for line in e:
			     words = line.split()
			     for i in words:
			         	if(i==Empid):
			         		print('emp id must be unique')
		e.close()
		if Empid<999:
			print('emp id must be more than 3 characters')
		else:
			addemplist['Employee_Id']=Empid
			empid=str(Empid)
			with open('empid.txt','a') as f:
				f.write(empid)
				f.write('\n')
			f.close()
		
		try:
			Sal= int(input('Enter employee Salary: '))
			if Sal<3000:
				print('Salary should be more than 3k')
			else:
				addemplist['Employee_Salary']=Sal
		except:
			print('enter valid salary')
		
		try:
			Deptno=int(input('Enter dept number: '))
			if(Deptno != 10 and Deptno!=20 and Deptno!=30):
				print('invalid dept number')
			else:
				addemplist['Dept_No']=Deptno
		except:
			print('enter valid dept number')
			
		print('Employee added', addemplist)
		file1= open('emp.txt','a')
		file1.write(json.dumps(addemplist))
		file1.close()
		
		
	def Display_Emp():
		#delete employee
		print('Displaying employee list\n')
		with open('emp.txt','r') as f:
			lines=f.readlines()
			print(lines)
		
		
		
	def Seperate_data():
		print('seperating data..')

print('1.  Add_emp')
print('2.  Display_emp')
print('3.  Seperate_data')
print('4.  Exit')
userinput=int(input())
if userinput==1:
	Employee.Add_Emp()
elif userinput==2:
	Employee.Display_Emp()
elif userinput==3:
	Employee.Seperate_data()
elif userinput==4:
	quit()
else:
	print('enter valid input')