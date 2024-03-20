#Day 8


# 1.) Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number
#1

#n=int(input("enter the number:")
#n1=n*n
#print("n:",n1)


#Eg:4
#function with return statement
# 1.) A variable can be declared inside the function can be outside the function using return
#2.) Return does not print anything
#3.) We cannot write any code below return statement
#def f1():
 #   z=8
#f1()
#print(z)# error---->Cannot use outside the function

#def f1(a,b):
 #   c=a*b
  #  return c
#print(f1(6,8))
#obj= f1(6,8)
#obj1 = f1(4,6)




#def gracemark(object):
 #   print(object+4)
#gracemark(obj)
#gracemark(obj1)


#123
#def palidrome(n):
 #   string = str(n)
  #  rev = str(n)[::-1]
   # if string==rev:
    #    print(n,"palidrome")
    #else:
     #   print("Not palidrome")
#a= int(input("Enter the value: "))
#palidrome(a)

# Based on the declaration of parameters and args
# Functions are divided into 5 categories

#positional args
#keyboard args
#default args
#variable length args
#keyboard variable length args

# Keyboard args
# The position of parameter achieve to same as position as argument
# Eg:1

#def profile(name,phone,mark):
  #  txt ="My name is{}.My phone number is {}. I got {} marks."
 #   print(txt.format(name,phone,mark))

#profile(8074884522,"Chandu",35)


# * todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "shashank", mark=99, phone=9876543210) # Error
# profile(9876543210,name= "shashank", mark=99) # error
# profile("shashank",mark=98,phone=9876543210)

# * default args
# the method of assigning the argument to parmeters wile declaring the
# function

# ! eg:1
# def profile(name,phone,place="kadapa")
#     txt ="my name is {}. my phone number is {}. i am from {}."
#     print("lokchand",8886750013,"hyderabad")
#     else:
#        print("you are not eligible  to sigup")
#profile("sharru",9390982720,)

# * variable length params
# ! Eg:1
# to pass more then 1 arg to paremeter means we use variable length args
# to convert normal paremeter to variable length param, add* to ther prefix of param

# name = "sharru", 'name2' 'name'3
#def profile(*name):
 #   for val in name:
  #      print("my name is",val)
#profile("sharru", "amma", "nanna")


#Eg:2

#def profile(*name,age):
 #   for val in name:
  #      print("My name is",val,"my age is",age)
#profile("chandu",'name', 'name3',19) #error----> age has no args

#def profile (age,*name):
 #   for val in name:
  #      print("My name is",val,"my age is",age)
#print(19,"chandu",'name2','name3')


#Keyword variable length args
# keyword args----> which is used to privide the args in the form of key value pair.


# Eg:1
#def price(**price_list):
#    print(price_list)

#price(shirt=1000, iphone=80000)


#n=5

#{1:1,2:4,3:9,4:1,5:5}

#def dict1(n):
    #d1 = {}
   # for val in range(1, n+1):
  #      d1[val] = val**2
 #   print(d1)
#dict1(5)

# ------->Object oriented programming

# The paradigms of object oriented programming are

#Class
#Objects
#Inheritance
#Polymorphism
#Abstraction
#Encapsulation

# Class is a blue print of an object

#l1 = [1, 2, 3, 4, 5, 6]

# Eg:1
#class c1:
  #  name1 = "Sindhu"
 #   print(name1)

#eg:2
 
#class person:
 #   name = "Sindhu"

#c = person()
#print(c.name)

#eg:3
#create of a method
#when the function is created with a class is called as method

#Method without parameter
#class person:
#    def display(person):
#        print("Hello welcome to classes")

#p = person()
#p.display()

# ? Eg:4
#Method with parameter
#class person:
 #   def display(person,name,age):
  #      print(name,age)


#p = person()
#p.display("chandu",19)

#Eg: 5
#class person1:
 #   fname = "Chandu" #attribute or static variable
  #  lname = "C"

   # def first_name(self):
    #    print(self.fname)

    #def full_name(self):
     #   print(self.fname+""+self.lname)

#p = person1()
#p.first_name()
#p.full_name


#Eg:66
     #Constructora--->_init_()
    #This is a special method which has the ability to excute itself without
     #calling it manually through thr process of instantation

class profile:
    def__init__(self):
        print("Hey")

p = profile()


 










