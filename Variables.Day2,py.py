#a, b=7, 8
#print(a, b)
#print(type(a))

#a, b, c = 9, 8, 7, 8
#print(a,b,c)

#a, b,=c=9,8
#print(a)
#print(b)
#print(c)


#a=b, c = 4, 2
#print=(a,b,c)


# 1 -->swapping of variables

#eg1;
#a=7
#b=5
#temp=a
#a=b
#b=temp
#print(a, b)

#temp=is used to replace the a,b values

#eg2;
#a= a+b   #a=12
#b= a-b   #b=12-5=7 
#c= a-b   #a=12-7=5

#print(a,b)

# a, b=b, a # only in python
# print(a,b)

#a=a*b  #a=35
#b=a/b  #b=35/7=5
#a=a/b  #a=35/5=7
#print(int(a), int(b))

 # 2 Id function; id()--> it is used to find memory address of the variable
 
#a = 7
#b = 8
#print(a)
#print(id(a))
#print(id(b))


 # 3 ----> Keywords
# Keywords are reserved words which provides special meaning to compiler or interpretor

 
#import keyword
#print(keyword.kwlist)
#print(len(keyword.kwlist))
#print(type(keyword.kwlist))

# To check if the string is keyword or not

#print(keyword.iskeyword("sid"))# false

  #if = 8
#print(if) # error coz if is a keyword

# 4 !--->Literals
#Literal is the constant value assigned to a variable
#A variable is consider to be constant when it is defines in caps
#in caps

#a=78 # a is variable
#A=78 # A is constant

#l1 = [5, 7, 8, 9]--> it is a list we can change the values inside the box 

#hash()--> it creates a hash vlue for constant data types and
#provides error for non constant data types
#n1 = 89+7j
#print(hash(n1))

#f1 = (7, 8, 9)

#print(hash(f1)) #error ---> list is non-constant or multiple data type

#a=9
#b=9
#print(id(a))
#print(id(b))

#Here the id were stored in the same location

#a=9
#b=8
#print(id(a))
#print(id(b))

#! 5 --> Operators
#Operators are symbols which is used to perform various opertaions
#between 2 or more operators

 #Arithmatic operator
 #Assignment operator
 #Logical operator
 #Relational or comparison operator
 #Bitwise operator
 #Identify operator
 #Membership operator

#* 6 --->Arithmatic--> +,-,*,/,%,//,**.

 #Example1

#a=8
#b=9
#c=2
#print(a+b+c)

#Examole2

#a=8
#b=9
#c=2
#print(a-b-c)

   #Example3

#a=8
#b=9
#c=2
#print(a*b*c)

   #Example4

#a=8
#b=9
#c=2
#print(a/b/c)

  #Example5

#a=8
#b=9
#c=2
#print(a%b%c)

 # input()--> used to get the runtime input
#n1 = int(input("Enter the value"))
#print(n1)

 # input()--> used to the runtime input
 # eval()--> used to get the runtime values of all datatype

#n1 = eval(input("Enter the value: "))
#print(type(n1))

#a=4
#b=2
#print(a/b)  # is used to get the quotient value
#print(a%b) #is used to get the remainder value

  
 #  ! // -->floor division

#a=765433
#b=19
#print(a/b)
#print(a//b) #-> the output will be in integer & the output will 
#be baased on floor value


 #!  7 **--> used for power of a number
 #print(2**4) #-->16

 # 8 ! Assignment-->= +=,-=,/=,*=,//=,**=,&=,|=

#a=8
#a+=2
#print(a)

#a=30
#a-=5
#print(a)


 # 9 Comparison --> ==, >, <, !=, <=, >=
#a = 8
#b = 7
#print(a>b)

#a = 9
#b = 5
#print(a==b)

  # 10 ! Bitwise operator -->&, |, ^, ~, <<, >>
#a = 7
#b = 4
#print(a&b)

#AND
#A B A&B
#0 0  0
#0 1  0
#1 0  0
#1 1  1

#OR
# A  B  A|B
# 0  0   0
# 0  1   1
# 1  0   0
# 1  1   1


#XOR
#A  B  A^B
#0  0   0
#0  1   1
#1  0   1
#1  1   0


#32  16  8  4  2  1  
# 0   0  1  0  1  0 #-->10
# 1   0  0  1  1  0^ #-->
#----------------

  
 
#2^4 2^3 2^2 2^1 2^0
#8   4   2   1

#0   1   1   1   #-->7
#0   1   0   0   #-->6&
#---------------
#0   1   1   1 #--> 7

#~-->
#a = 9876
#print(~a)

#a = 9

# 128 64 32 16 8 4 2 1
#  0   0  0  0 1 0 0 1 #-->9

#  1   1  1  1 0 1 1 0 #-->-10

#  0   0  0  0 1 0 0 1-->10

#  1   1  1  1 0 1 --> 1s compliment of 10
               # 1 --> 2s compliment
#-----------------------------

#      1  1  1  1  0 1 1 0 --> -10


# 256 128 64 32 16 8 4 2 1
#  0   0   0  0  0 0 1 0 1  3<<
#  0   0   0  1  0 1 0 0 0 --> 40
# 107

# <<,>>
# print(5>>1)
# print(16>>4)

 # 11 ! Logical operator
 # and, or, not

#a = 6
# print(a is > 3 and a is <10)
# print(a>7 or a<30)
# print(not (a>8 and a<10))


 # 12 ! Identity operator
 #It is used to compare the memory location that the values are stored
 # is, is not
#a = 8
#b = 8
#print( a is b )
#print(a==b)

#a=[1, 2, 3]
#b=[1, 2, 3]
#print(a is b)

 #a = [1, 2, 3]
 #b = [1, 2, 3]
 #print(a is not b)

 #13  Membership Operator
 # in, not in
#l1 = [7, 8, 9, 0, 6, 5]
#num = 55
#print(num in l1)

#l1 = [7, 8, 9, 0, 6, 5]
#num = 55
#print(num not in l1)

 #num=678
 #print(8 in num) #error

 # ! 14 Conditional statement
 # if, elif, else

 #Eg;-1
 #--> c syntax
 # if (condition){
 #     statement;
 #     statement;
 #     statement;
 #}
 #python syntax
 # if condition: 
 #    statement;
 #    statement;
 #  statement;

# Eg: 1
#a = 6
#if a:
 #   print("hello")

 #Eg:2
 #a = 6
 #if a >3:
 #print("yes")
 #else:
 #print("no")
 
#EG:3
# if 7>8:
#print("hello")

#print("no")


#Eg:4
# a = 0
# a = none
# a = false
# a = ""
# if a:
#print("yes")
#else:
#print("no")

#a number is even or odd sum1
#n=int(input("Enter the number: "))
#if n %2==0:
 # print(n," is even")
#else:
 # print("the number is odd")


#sum 2
 
#a=str(input("Enter your name: "))
#b=int(input("Enter your age: "))
#c=str(input("Enter your nationality: "))
#if b >=18 and c=="Indian":
 #   print("you are eligible for vote")
#else:
 #   print("not eligible")

    





