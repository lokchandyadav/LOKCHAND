  # EX:3
# Take values of lenght and breadth of a
#from user and check if it is square or not
#a=int(input("Enter the length : "))
#b=int(input("Enter the breadth : "))
#if a == b:
 #   print("This is square")
#else:
 #   print("This is not square")

# Ex:4:
#Python program to check whether the
#Given integer is a multiple of both 5 and 7

#a=int(input("Enter the number:"))
#if a%5==0 and a%7==0:
 #   print("Yes")
#else:
 #   print("No")

#Ex:5
 #write a program to accept the cost price of a bike and display
 #the road tax to be paid
 #according to the following criteria:
 # cost price (inRS)                  Tax
 #>100000                            15% + Discount 6%
 #>50000 and <=100000                10%
 #<=50000                             5%

#a=int(input("Enter the bike value: "))
#if a>=10000:
 #   discount = 100000*(6/100)
  #  value = a-discount
  #  tax = value *(15/100)
   # total= value + tax
#else:
 #   tax=a*(5/100)
  #  total = a*tax
#print("The on road cost of bike is : ",total)


# ---> if elif else
#a=7
#b=9
#c=2

#if a>b and a>c:
 #   print("a is greater ")
#elif b>a and b>c:
 #   print("b is greater ")
#elif c>a and c>b:
 #   print("c is greater ")

# A school has following rules for grading system:
# a. Below 25 -F
# b. 25 to 45 -E
# c. 45 to 50 -D
# d. 50 to 60 -C
# e. 60 to 80 -B
# f. above 80 -A
# Ask user to enter marks and print the corresponding grade.

#student=int(input("Enter the student marks: "))
#if student==25:
 #   print("You got F grade")
#elif student>=25 and student<=45:
 #   print("You got E grade")
#elif student>=45 and student<=50:
 #   print("You got D grade")
#elif student>=50 and student<=60:
 #   print("You got C grade")
#elif student>=60 and student<=80:
 #   print("You got B grade")
#elif student>=80 and student<=100:
 #   print("You got A geade")
#else:
 #   print("Fail")

# ! ---> Short hand if else
#Eg:1
#a=9
#b=60
#if a>b:
#print("A")
#else:
#print("B")


# ? ---> using short hand if else
#* Rules
#1.) Statement inside the if condition have to be present at first
#2.) elif cannot be used in short hand if else
#3.) Always it have to end with else

#print("A") if a>b else print("B")


# ! code to check the given char is vowel or consonent
#char = input("Enter the char: ")
#if char =="a" or char=="e" or char=="i" or char=="o" or char=="u":
#print("is vowel")
#else:
#print("is consonent")


# ? or

#str1 ="aeiouAEIOU"
#if char in str1:
 #   print("vowel")
#else:
 #   print("consonent")


# ! shorthand if else
#char = input("Enter the char: ")
#str1 = "aeiouAEIOU"
#print("vowels") if char in str1 else print("consonent")

# ! ---> elif ladder using short hand if else
#ex:1
# ? Find greatest among 3 variables using short hand if else
#a=8
#b=5
#c=9

#print("A is greater ") if a>b and a>c else print("B is greater") if b>a and b>c else print("c")is greater")

 # ! ------> Looping

# Looping can be implemented using
# for loop
# while loop


#--->for loop
# for loopis used to iteration, if we know the number of times the loop have to run
# It is used to iterate the iterables eg(string, list, tuple, etc...,)


#todo--> Syntax for loop
#for syntax in c:
#for(i=0;i<10;i++){
 # print("hello");
#}

 # ! for syntax in python
 #for userdefined_variables in range(start, end, step):default setup value is 1
   #  statement
  #   statement
 #    statement

 #Eg:1
 #To print the values from 1 to 100 using for loop
 
#for i in range(0, 10): #(n, n-1)
 #   print(i)
#print("hello")

 #Eg:2 For increment the values
 
#for val in range(23, 50, 2):
 #   print(val)

#for val in range(1, 50, 3):
 #   print(val)

# Eg:3 For decrement the values

#for val in range(10, 0, -1):
 #   print(val)

#for val in range(10, 0, -2):
 #   print(val)

# Eg: 4
# print the output of 7th multiplication table from 21 to 43
#for val in range(21, 43+1):
 #   print(val*7)

#for val in range(1, 10+1):
 #   print(val*7)

#for val in range(1, 10+1):
 #   print("the value is :",val*7)

#for val in range(1, 10+1):
 #   print(' 7 ', 'x',val,'=',val*7)#---> method 1
  #  ans="7x{}={}"
   # print(ans.format(val,val*7))-->method 2

#for val in range(1, 10+1):---> method 3
 #   print(f"7 x {val}={val*7}") 



#Eg:5
 #Break statement--> which is used to terminate the loop
#for val in range(1, 10):
 #   if val ==6:
  #      break
   # print(val)

#EG:6

#for val in range(1, 10):
 #   print(val)
  #  if val ==6:
   #     break


#Eg:7

#for val in range(1, 10):
 #   if val ==6:
  #      print(val)
   #     break

#Continue statement
   #Eg:1
#for val in range(1, 10):
    #if val ==6:
     #   continue
    #print(val)

#Eg:2
#practice problem
     
#print the even number between 20 to 40

#for val in range(20, 40):
 #   if val %2==0:
  #      print(val)

# print the odd numbers between 20 to 40

#for val in range(20, 40):
 #   if val %2!=0:
  #      print(val)     


#-----> While loop
# while loop is used when we do not know the number of times the
#loop have to run
# To iterate the non iterable elements while loop is used

# todo syntax

#initialization
#while condition:
#      statement
#      increment or decrement

# ! Eg:1
#to iterate number from 1 to 10

#i=0
#while i<11:
#    print(i)# or i+=1

#eg:2
# to decrement using while loop
#10,1

#i=10
#while i>0:
 #   print(i)
  #  i-=1


#-----> 1-4+9-16+25=15
#n=int(input("enter the number"))
#sum=0
#for val in range(1, n+1):
 #   sq=val*val
  #  if val %2!=0:
   #     sum=sum+sq
    #else:
     #   sum=sum-sq
#print(sum)

     

      



# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Print the reverse of given number --> n1= 234 o/p --> 432
        

#Assesment1, problrm 3


#for val in range(12, 37):
 #   if val %2==0:
  #      print(val)
        
#for val in range(12,37+1):
  #  if val %2!=0:
   #     print(val)






   


#Assesment1, problem5
   #Reversed command is used to change the values from left to right
   
n1=input("Enter the number: ")
n1_reversed=n1[::-1]
print(n1_reversed)



















