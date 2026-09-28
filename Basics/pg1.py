# 08-09-2025

# variable in python are first identifiers (name) that reference a memory location.

# Each Variable have: 
#   1. ID(Memory location)
#   2. Type(the type of value)
#   3. Data(the value it holds)


# Note: "is" operator is used to check the memory location
#       "==" is used to compare values

'''
a=5 # a is referencing integer type of object (5)
print(id(a))
print(type(a))
print(a)

b=5
print(id(b))
print(type(b))
print(b)
print(a is b)


c=10
d=c

print(id(c))
print(type(c))
print(c)

print(id(d))
print(type(d))
print(d)

#1 wap to check r process with a=10000, b=100000

a=10000 # a is referencing integer type of object (5)
print(id(a))
print(type(a))
print(a)

b=100000
print(id(b))
print(type(b))
print(b)
print(a is b)

# ----

x="xyz"
print(id(x))
print(type(x))
print(x)

y="xyz"
print(id(y))
print(type(y))
print(y)


#---

a=5
b=a
print(id(a))
print(id(b))

a=a+1
print(id(a))
print(id(b))
print(id(6))



# example program: (Define Memory Utilization Step by Step)

p=1 # here p is referencing interger type of object (1)
q=2 # here q is referencing interger type of object (2)
r=1 # here r is referencing interger type of object (1)
s=2 # here s is referencing interger type of object (2)
t=p # here t is referencing interger type of object (1)
u=s # here u is referencing interger type of object (2)

print(id(p))
print(id(q))
print(id(r))
print(id(s))
print(id(t))
print(id(u))

'''

# points to Understand: 
'''
1. Everything in Python is object
2. Variables are names only that reference to a object, they dont store value directly
3. In python, we have Multiple(Changeable / can be modified after creation) and Immutable(Cannot modify after creation)
'''
# 3.a>

# Int is a immutable data type in python 
# List is mutable
# example1:  

'''
a=5 # integer type of object(5)
print(id(a))
print(a)
a=a+1 # integer type of object(here we have modified its value)
print(id(a))# address after modification
print(a)

list1=[1,2,3] # list type of object
print(id(list1))
print(list1)
list1.append(5) # modifying value of list after initilization
print(id(list1)) # address of list after modification
print(list1)
'''
# Example 2: 

'''
x="xyz"
print(id(x))
print(x)
x="xyzqqq"
print(id(x))
print(x)

list1=["x", "f", "t"]
print(id(list1))
print(list1)
list1.append("d")
print(list1)

'''
'''
HW -----

WAP a program to create a string with the value "Hello"
now convert the string to upper case using function .upper()
store the value of function.upper to a new variable and check 
seperate object is created in memory or not and why
'''


# 12-09-25

'''
operation: special symbols eg(+,-,*,/) used to perform specific task on operands.
operands: eg(a,b) on which uniform operation

In Programming we have variables used in place of operands.
eg: a+b, a-b

Types of Operatos on the basis of number of operands
1. Unary Operator -- Need of only one operand
# Note: There is no Pre- increment, Post increment etc..
eg: a++
    a=a+1 or a+=1
    a=a-1 or a-=1

2. Binary Operator -- Required two operands for operation
eg: Arithematic, Comparison

3. Ternary Operator -- Required three or more operands to perform operation
eg: Logical Operator


Types of Operator on the basis of behaviour.

1. Arithmatic Operator-> 
    + Addition
    - Subtraction
    * Multiplication
    / Division eg: 10/3= 3.33
    // floor division eg: 10//3= 3
    % Modulus eg: 10%3->1 (works with integer value only)

2. Exponential eg: Provide left with power of right variable
    eg: 10**3=1000

3. Assignment Operator: 
    = assign value of right side operand to the operand present at the left side
    eg: a=1
        b=a(= will assign value of a to b)

Arithmetic Assignment operator or SHORTHAND operators
    +=  eg a+=4 same as a=a+4
    -=  eg a-=4 same as a=a-4
    *=  eg a*=4 same as a=a*4
    /=  eg a/=4 same as a=a/4
    %=  eg a%=4 same as a=a%4
    //= eg a//=4 same as a=a//4
    **= eg a**=4 same as a=a**4

Relational Operator as Comparison Operaror

    are binary operator return boolean value TRUE/FALSE
    1. > Greater Than 
    2. < Less Than 
    3. >= Greater than or equal to
    4. <= Less than or equal to
    5. != Not equal to
    6. == equal equal (check operator)

    eg: a=1
        b=2
        c=3
            "AND"
            a>b and b>c and c<a
            1. and will return false of all the conditions are false

            a<b and b<c and c<a
            2. and will return false if any of condition is false

            a<b and b<c and c>a 
            3. and will return true if all the conditions are true

            "OR"
            a>b or b>c or c<a
            1. or will return false of all the conditions are false

            a<b or b<c or c<a
            2. or will return true if any of condition is false

            a<b or b<c or c>a 
            3. or will return true if all the conditions are true

            "NOT"- opposite of "OR"

            a>b not b>c not c<a
            True

            a<b not b<c not c<a
            False

            a<b not b<c not c>a
            False

'''

# Different Programming Style

'''
1. Sequental Programming 
follows the flow of instructions sequentially

2. Conditional Programming
implemented with the help of conditional constructs
a. if
b. if else
c. nested if else
d. elif ladder
e. match case

3. Iterarive (Repetitive Task)
a. for
b. while

'''
#Example Programs to understand sequential Programming

'''
a=1
b=2
c=3
d=a+b
a+=5 # here we have updated the value of a
b*=3 # here we have updated the value of b
d=a+b # in this step d will consider the updated value of a and b
print(a)
print(b)
print(c)
print(d)'''

''' Example Programs
    1.  Write a program to accept user name and print Welcome message with username
    2.  Write a program to accept price of 5 items for the user
        calculate sum and apply 10 discount on amount and print discount and final price
    3.  Write a program to accept class duration in hours from user and duration of class 
        in minutes
    4.  Write a program to accept date of year from user calculate age anf print number of days
    5.  Write a program to accept user details like Name, Address, Mobile Number, Stream, College
        Name and display the detail entered by user in proper format using format character or format
        sequence

'''
'''
#1.
x=input("Enter the User Name: ")
print("Welcome To Python", x)

#2. 
x1=int(input("Enter the Price of 1st Item: "))
x2=int(input("Enter the Price of 2nd Item: "))
x3=int(input("Enter the Price of 3rd Item: "))
x4=int(input("Enter the Price of 4th Item: "))
x5=int(input("Enter the Price of 5th Item: "))
sum = x1+x2+x3+x4+x5
discount=sum*0.1
print("Sum: ",sum,  "After Discount: ", sum-discount)

#3
nandu= int(input("Enter Class duration in hours: "))
print("Class duration in Minutes: ", nandu*60)

#4
year=int(input("Enter your Year of Birth: "))
age=2025-year
print("Age(in years): ", age, "\nAge(in days): ", age*365)

#5.
y1=(input("Enter your Name: "))
y2=(input("Enter Address: "))
y3=(input("Enter Mobile Number: "))
y4=(input("Enter your Stream: "))
y5=(input("Enter College Name: "))

print("\n--- User Details ---")
print("Name: ", y1)
print("Address:", y2)
print("Mobile Number:", y3)
print("Stream: ", y4)
print("College Name: ", y5)

'''
# 15-09-25

# sequential Programming: follows a order of statement works in sequental pattern. 
# flow control: where there is a decision of selecting statement depending upon the condition.
# in simple terms, here the execution of statement is depndent on a condition, condition decided which statement to be executed.
# types of Flow Control: 
# 1. Selection(condition)
# 2. Iteration / Repetitions(Loop)
# 3. Jumping Statement (transfer flow from a point to another)

'''
1. Selection Statement
    a. if
    b. if else
    c. elif ladder
    d. nested if else
        types of nested if:
            i. if inside if
            ii. if else inside if
            iii. if else inside if else
            d. match case 3.10+
'''

# Decision Making Programming
'''
if statement 
    syntax: 
            if condition
            statement 

    Note: After if block or any other flow of control condition
    First use: after condition
    then use space (indedation) to place statement
    here space decides block like other programming eg: C/ C++
    we dont have { } to decide block
'''
# Example Program if

# n=int(input("Enter a Number: "))
# if n>0:            # condition
#     print("Number is +ve")      # dependent Statement



# if else
'''
synatx
        if conditon:
            statement or statements
        else:
            statement
'''
#Example program if else:

# n=int(input("Enter a Number: "))
# if n>0:            # condition
#     print("Number is +ve")      # dependent Statement
# else:
#     print("Number is -ve")

# nested if else
'''
a. if inside if
syntax: 
        if conditon:
            if condition:
                        statement
'''
# Example Program if inside if

# n= int(input("Enter the Number: "))
# if n>0:
#     if n%2==0:
#         print("Number is +ve and Even ")
#     else: 
#         print("Number is +ve and Odd ")
# else:
#     print("Number is Negative ")

# c. if else inside if else

'''
Syntax 
if condition:
    if condition:
        statement
e
'''

# elif ladder
'''
used to check multiple conditions
syntax: 
if condition:
    statement
elif condition: 
    statement
.
.
else
    statement
'''

# example program elif ladder:
'''
n=int(input("Enter the Number: "))
if n==1:
    print("One")
elif n==2:
    print("Two")
elif n==3:
    print("Three")
else:
    print("Number is not between 1 to 3")

'''

# Match Case 
# used to check multiple conditions
'''
Syntax
Match Variable:
    case case consunent:
    statement
    case case consunent:
    statement
    case __:
    statement
'''

# Note: In match case we dont use break as in python we dont have fall through that we face in C, C++
#Example Program match case

# n=int(input("Enter Number: "))
# match n:
#     case 1: 
#         print("One")
#     case 2: 
#         print("Two")
#     case 3: 
#         print("Three")
#     case _: 
#         print("Invalid Value entered not in Between 1 to 3")

'''
List of Programms understand different control Statement
1. Understand Required Decision making Approach
2. Write your Logic for truth value and falsy value

Q1. Write a Program to accept Registration Number and percentage from student according to below defined criteria,
assign them club 
a. Registration Number between 1 to 50 and percentage between 80 to 100: IEEE CLUB
b. Registration Number between 51 to 100 and percentage between 70 to 80: ECO CLUB
c. Registration Number between 100 to 150 and percentage between 80 to 90: NCCE CLUB
d. Registration Number between 151 to 200 and percentage between 90 to 100: NSS CLUB
To check all these condition first ask user to enter a Pin equal to 123
'''
'''
n=int(input("Enter Registration Number: "))
p=int(input("Enter Percentage: "))
pin=int(input("Enter Pin: "))
if pin==123:
    if n<=50: 
        if p>80 & p<=100:
            print("Congrats You got IEEE Club")
    elif n>50 & n<=100: 
        if p>70 & p<=80:
            print("Congrats You got ECO Club")
    elif n>100 & n<=150: 
        if p>=80 & p<=90:
            print("Congrats You got NCCE Club")
    elif n>150 & n<=200: 
        if p>=90 & p<=100:
            print("Congrats You got NSS Club")
    else:
        print("Invalid Input !!!")


# '''

# st="WELCOME" # MELCOME
# # print(st[-2:]+st[2:-2]+st[:2])
# print(st[2:])
# for i in st:
#     print(i)

# st= "welcome to the world of python"
# print(st.capitalize())
# print(st.upper())
# st=(st.lower())
# print(st.lower())
# print(st.title())
# st=st.title()
# print(st.swapcase())

# st="mississippi"
# print(st.count("S",6,8))
# print(st.index("si",4))

# st="hello"
# print(st.ljust(40))
# print(st.center(40))
# print(st.rjust(40))

# st="hello"
# print(st.ljust(40,"-"))
# print(st.center(40,"*"))
# print(st.rjust(40,'.'))


# st="jammu,noida,dehradun,akhnoor,bhalwal,sungal,sohal"
# re=st.split(",")
# print(re)
# st1="-".join(re)
# print(st1)

# name="nandu"
# age=19 
# st="My name is %s and i am %d year's old "%(name, age)
# st1="My name is {} and i am {} year's old ".format(name, age)
# st2=f"My name is {name} and i am {age} year's old "
# print(st)
# print(st1)
# print(st2)


# st="malayalam"
# print(st.strip())

# st="malayalam"
# print(st.strip("ml"))

# print(st.replace("a","i"))
# st="abracadabra"
# print(st[0]+st[1:].replace(st[0]))      

'''
lst=[10,20,30]
t=tuple(lst)
print(t, type(t))

t=10,20,30
print(t)
t=(10) ## not a tuple of single len
t=(10,) # tuple of single length
t=10, # also tuple of single length
print(t)

t= tuple(range(2,11,2))
print(t)
for num in t:
    print(num, end= " ")
print()
print(t[0], t[-1], t[0:2], t[-2:], t[::-1], sep="\n")

tup=(10, 12.5, 12+5j, True, "Jamse", [12, 23, 24])
# for i in tup:
#     print(tup, type(tup))

# tup[0]=tup[0]+10 # error... not  work,
tup[-1].append(100)
print(tup)

t=10, 20, 30, 40 , 50
print(t)
a,b,*c=t
print(f"a:{a} b:{b} c:{c}")
'''


#swapping
'''
num1=int(input("Enter first Number: "))
num2=int(input("Enter Second Number: "))
print(f"before swapp num1={num1} num2={num2}")
num1, num2= num2, num1
print(f"after swap num1:{num1} num2:{num2}")
'''

#fibonacci

# num1,num2=0,1
# for i in range(10):
#     print(num1, end=" ")
#     num1, num2=num2, num1+num2
num1=0
num2=1
for i in range(10):
    print(num1, end=" ")
    temp=num1
    num1=num2
    num2=temp+num2


# firpass=input("")
# geta=len(firpass)
# str=""
# for i in range(geta):
#     if firpass[i] == 'a':
#         str+='e'
#     elif firpass[i] =='e':
#         str+='e'
#     elif firpass[i] =='i':
#         str+='o'
#     elif firpass[i] =='o':
#         str+='u'
#     elif firpass[i] =='u':
#         str+='a'
#     elif firpass[i] =='A':
#         str+='E'
#     elif firpass[i] =='E':
#         str+='I'
#     elif firpass[i] =='I':
#         str+='O'
#     elif firpass[i] =='O':
#         str+='U'
#     elif firpass[i] =='U':
#         str+='A'
#     else:
#         str+=firpass[i]


# print(str)
