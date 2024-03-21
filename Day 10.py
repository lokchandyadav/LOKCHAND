# Day:10
'''
#Method over-riding
#Polymorphism in classes using inheritance


class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("Sbi rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()

'''
'''
#Eg:2
class USA:
    def language(self):
        print("ENglish")

    def capital(self):
        print("Washington DC")

class INDIA:
    def language(Self):
        print("None")

    def capital(self):
        print("New Delhi")

I = INDIA()
I.language()
I.capital()
'''

#Eg"3
# polymorphism using objects

#c1,c2---> c1 = print(c1),print(c2)
#f1,f2

'''
class c1:
    def f1(self):
        print("class1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class2")

obj1 = c2()
obj2 = c1()


'''

'''
#Eg:4
class c1:
    def f1(self):
        print("class1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class2")

obj1 = c2()
obj2 = c1()

def display(a):
    a.f1()
display(obj1)
display(obj2)
'''


# changing the functionality of builtin functions
'''
a = 9
b = 6
#print(a+b)
print(a.__add__(b)) # dunder method or mafic method


int()
#print(a.__sub__(b))
len()


class shopping:
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length
s = shopping([1,2,3,4,5])
print(len(s))
'''
'''

# ----> Method over loading
# Eg:1
class suming:
    def add(self,a,b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)

s = suming()
#s.add(4,3)# -------> error
s.add(4,5,1)

'''
'''

#Eg:2
class suming:
    def add(self, a=None, b=None, c=None):
        if a != None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj = suming()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)


'''

#---->Abstraction

# The process of hiding the implementation detail is abstraction


# Eg:1
'''
from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")

    def name(self):
        print("iam triangle")

    def sides(self):
        pass

class square(shapes):
    def square(self):
        print("4 sides")

    def sides(self):
        pass

tr = triangle()
tr.triangle_sides()
tr.name()
'''
# ! rules to define abstract class1
#1.) abstruct class cannot be instantiated
#2.) from abc import ABC, abstactmethod
#3.) subclass the normal class with ABC
#4.) convert the normal method inside the abstract class to abstract method
#5.) all the child classes have to be subclassed with abstract class
#6.)the abstract method should be present in the in child classes

# ! Eg:2
#super() --> used to acces the parent class method from child class method
#form abc import ABC, abstractmethod
'''
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("this is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")
        
    def m1(self):
        pass

class2 = c2()
class2.m2()
'''
'''
# *Eg:3
#
from abc import ABC, absractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "chandu1174$"
        return pswd

class login(password):
    def validate(self, name, passwrd):
        if super().pwd() == passwrd:
           print("welcome", name,'!!')
           print("login successfull")
        else:
            print("please check the password")

    def pwd(self):
        pass

login = login()
name = input("enter the name: ")
pwd = input("enter the password: ")
login.validate(name, pwd)
        


'''
# ! Encapsulation
# * ---> Eg:1
'''
class car:
    __name = "BMW" # private variable
    print(__name)
    
c1 = car()
print(c1.name) #  error
c1.name = "AUDI"
print(c1.name) # error
'''
# * ---> Eg:2
# ? accessing private date outside the class
'''
class c1:
    __phone = '9900335522'

    def display(self):
        print(slef.__phone)
c = c1()
c.display()
'''
# * ---> Eg:3
# ? declare private method
'''
class class1:
    def m1(self):# private method
        print("iam private method")

    def __intit__(self):
        self.__m1()

c = class1()
c.__m1()# error
'''


















# ? nestd class
'''
class class1:
    class class2:
        name = "lord shiva"

        def dispaly (self):
            print(self.name)
    obj1 = class2()

obj = class1()
obj.obj1.
'''
d1 = {"shirt":1000, "pant":1500, "Shoes":900, "handkey":30}
for val in d1:
    if d1[val] == min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)


# To write the capital letters
'''
def decor(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner()

@decor
def greet():
    return 'good morning'

print(greet)
'''




#) Tasks
#Write the code for the belwo tasks using function
#1.)>d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'

#2.) Find then 67, is strong number or not

#3.) 11 = [1,2,3,4,5,6]
#n=2 --> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]
