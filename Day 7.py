# Day7

# ----> Assesment
# 1.) d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


#d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#d1.update(d2)
#print(d1)



#2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions


#set1 = {'Python', 'Java', 'Data Science'}
#set2 = {'ML', 'AI', 'R Language', 'Python'}
#set3 = {'Data Analytics', 'Robotics', 'Deep L'}
#c = 0
#flag = 0
#for val in range(3):
 #   c=c+1
  #  if c==1:
   #     for val in set1:
    #        if val in set2 or val in set3:
     #           flag=1
      #          break
    #if c==2:
     #   for val in set2:
      #      if val in set1 or val in set3:
       #         flag=1
        #        break

    #if c==3:
     #   for val in set3:
      #      if val in set2 or val in set1:
       #         flag=1
        #        break
#if flag==0:
 #   print("disjoint")
#else:
 #   print("Joint")


#3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3 = []
#for val in range(len(list1)):
 #   ans = list1[val]+list2[val]
  #  l3.append(ans)
#print(l3)

#or

#i=0
#while i<len(list1):
  #  l3.append(list[i]+list[i])
 #   i+=1
#print(l3)

#Funtions
 #DEF
 #Function is a block of code which is used to perform a specific functionality
 #Function can be created using def keyboard

 #Functions has 3 parts
 # Function declaration
 # Function definition
 # Function call

def greet():
    print("welcome User!!")
    
greet()
greet()
greet()
greet()
greet()
greet()
greet() # function calling


#Eg:2
# ? Function with parameter


#def greeting(name):
#    print("welcome",name)


#for val in range(1):
#    username=input("Enter the name:")
#    greeting(username)


#!Eg:3

def profile(name,age,place):
    print(name,age,place)
profile("sid",29,"cbe")
# 1.) Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number



 
