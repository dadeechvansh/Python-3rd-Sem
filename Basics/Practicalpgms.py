# Exp No:- 1 Write a program to demonstrate type checking of various data types and demonstrate the use of 
# following built in functions in python: abs(), len(), min(), round(), isalnum(), type().

#(nahi karna) Exp No: 2 Write a program to illustrate iteration over the list and dictionary.

# Exp No:- 3 Consider the string to Python Perform the following operations: Count the number of alphabets in 
# the given string. To extract characters in the given, range from the given string. Check if the string is alphanumeric or not.

# Exp No 8- Write a python program to convert temperature to and from Celsius to Fahrenheit

# Exp No 10 Write a program to create a Simple Calculator using a switch case and function for every operation

# Exp No 11- Write a python program that accepts the length of three sides of a triangle as inputs. The program 
# should indicate whether or not the triangle is a right-angled triangle. (Use Pythagorean theorem) 
# Also find out its area using HERON FORMULA


# ANS 1: 

# a = 10
# b = 3.14
# c = "Hello123"
# print(type(a))
# print(type(b))
# print(type(c))

# # abs
# print(abs(-25))

# # len()
# print(len("Python"))

# # min()
# print(min(5, 8, 2, 9))

# # round()
# print(round(12.5678, 2))

# # isalnum()
# print("Vansh123".isalnum())
# print("Vansh 123".isalnum())

#ANS 3: 

# str=input("Enter the String: ")
# leng=len(str)
# print("Length Of String: ",leng)

# start=int(input("Enter the Starting Range to Extract: "))
# end=int(input("Enter the Ending Range to Exrtact: "))
# print(str[start:end])

# print("Alphanumeric: ", str.isalnum())



#ANS 8:

# choice=int(input("Enter Your Choice (1 - Celcius To Fahrenheit / 2 - Fahrenheit To Celcius ): "))
# if choice==1:
#     c = float(input("Enter Temperature in Celsius: "))
#     f = (9/5) * c + 32
#     print("Temperature in Fahrenheit:", f)
# elif choice==2:
#     f = float(input("Enter temperature in Fahrenheit: "))
#     c = (5/9) * (f - 32)
#     print("Temperature in Celsius:", c)
# else:
#     print("Invalid Choice !!!")




# ANS 10

# print("Simple Calculator")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter your choice (1-4): "))
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# match choice:
#     case 1:
#         print("Addition:", a + b)
#     case 2:
#         print("Subtraction:", a - b)
#     case 3:
#         print("Multiplication:", a * b)
#     case 4:
#         if b != 0:
#             print("Division:", a / b)
#         else:
#             print("Error! Division by zero.")
#     case _:
#         print("Invalid choice!")



# ANS 11




# s1 = int(input("Enter ist side of triangle : "))
# s2 = int(input("Enter 2nd side of triangle : "))
# s3 = int(input("Enter 3rd side of triangle : "))

# h = max(s1,s2,s3)
# b = min(s1,s2,s3)
# p = (s1+s2+s3)-(h+b)
# print(f"H : {h},P : {p},B : {b}\n")

# if(h**2 == (p**2 + b**2)):
#     print("The triangle is right angled\n")
#     s = (h+p+b)//2
#     ps = s*((s-h)*(s-b)*(s-p))
#     area = ps**0.5
#     print("Area : ",round(area,2))
# else:
#     print("The triangle is not right angled\n")


# print(ord('a'))

# prac 6,7
# database=[]

# def createdb():
#     count=int(input("Enter the Total no. of Students: "))
#     record={}
#     for i in range(count):
#         record["rno"]=int(input("Enter Roll No.: "))
#         record["name"]=input("Enter Name: ")
#         record["brach"]=input("Enter Branch: ")
#         record["sem"]=int(input("Enter Semester: "))
#         record["cgpa"]=float(input("Enter CGPA: "))
#         database.append(record)
#         print("")

# def printdb():
#     for rec in database:
#         print(rec)

# def searchstudent():
#     rno=int(input("Enter the Roll Number to search the record: "))
#     for rec in database:
#         if rec['rno']==rno:
#             print(rec)
# createdb()
# printdb()
# searchstudent()


23-11-25
# Exp 5:  WAP to reverse the matrix

# n = int(input("Enter size of matrix (rows = columns): "))
# matrix = []
# print("Enter matrix elements:")
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)
# k = int(input("Enter k value: "))
# for i in range(n):
#     if (i + 1) % k == 0:
#         matrix[i] = matrix[i][::-1]
# print("\nMatrix after reversing every k-th row:")
# for row in matrix:
#     print(row)

#exp 2

# numbers = [10, 20, 30, 40, 50]

# print("Iterating over list:")
# for num in numbers:
#     print(num)
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "BCA"
# }

# print("\nIterating over dictionary:")
# for key, value in student.items():
#     print(key, ":", value)


# exp 4:


# n = int(input("Enter number of elements: "))
# arr = []
# print("Enter elements:")
# for i in range(n):
#     arr.append(int(input()))
# key = int(input("Enter element to search: "))
# found = False
# for i in range(n):
#     if arr[i] == key:
#         print("Linear Search: Element found at index", i)
#         found = True
#         break
# if not found:
#     print("Linear Search: Element not found")
# arr.sort()
# print("\nSorted array for Binary Search:", arr)
# low = 0
# high = n - 1
# found = False
# while low <= high:
#     mid = (low + high) // 2
#     if arr[mid] == key:
#         print("Binary Search: Element found at index", mid)
#         found = True
#         break
#     elif arr[mid] < key:
#         low = mid + 1
#     else:
#         high = mid - 1
# if not found:
#     print("Binary Search: Element not found")

# exp 7
# import os

# database = []

# def createEmpDB():
#     empid = input("Enter Employee ID: ")
#     name = input("Enter Employee Name: ")
#     salary = float(input("Enter Salary: "))
#     dept = input("Enter Department: ")
#     contact = input("Enter Contact Number: ")
#     email = input("Enter Email ID: ")

#     record = (empid, name, salary, dept, contact, email)
#     database.append(record)

# def printDB():
#     os.system('cls')   # use 'clear' for Linux/Mac

#     print("Employee Database".center(80, "-"))
#     print()

#     print(f"{'Emp ID':<10}{'Name':<15}{'Salary':<10}{'Dept':<15}{'Contact':<15}{'Email':<25}")
#     print("-" * 90)

#     for emp in database:
#         print(f"{emp[0]:<10}{emp[1]:<15}{emp[2]:<10}{emp[3]:<15}{emp[4]:<15}{emp[5]:<25}")

#     print("-".center(80, "-"))

# # Main Program
# createEmpDB()
# printDB()

# exp 9

# # Base class
# class Employee:
#     def __init__(self, name, salary, dept, contact, email):
#         self.name = name
#         self.salary = salary
#         self.dept = dept
#         self.contact = contact
#         self.email = email

#     def display(self):
#         print("\nEmployee Details")
#         print("Name    :", self.name)
#         print("Salary :", self.salary)
#         print("Dept    :", self.dept)
#         print("Contact :", self.contact)
#         print("Email   :", self.email)


# # Child class (Inheritance)
# class Manager(Employee):
#     def __init__(self, name, salary, dept, contact, email, bonus):
#         # Calling parent class constructor
#         super().__init__(name, salary, dept, contact, email)
#         self.bonus = bonus

#     def total_salary(self):
#         return self.salary + self.bonus


# # Taking input
# print("Enter Employee Details")
# name = input("Enter name: ")
# salary = int(input("Enter salary: "))
# dept = input("Enter department: ")
# contact = input("Enter contact number: ")
# email = input("Enter email: ")
# bonus = int(input("Enter bonus: "))

# # Object creation
# emp = Manager(name, salary, dept, contact, email, bonus)

# # Display result
# emp.display()
# print("Bonus   :", bonus)
# print("Total Salary :", emp.total_salary())

# exp 6

# Create empty dictionary
students = {}

# Number of students
n = int(input("Enter number of students: "))

# Input student records
for i in range(n):
    roll = input("\nEnter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    students[roll] = {"Name": name, "Marks": marks}

# Display all students
print("\nStudent Records:")
print(students)

# Searching a student
search_roll = input("\nEnter Roll Number to search: ")

if search_roll in students:
    print("\nRecord Found:")
    print("Name  :", students[search_roll]["Name"])
    print("Marks:", students[search_roll]["Marks"])
else:
    print("\nRecord Not Found")
