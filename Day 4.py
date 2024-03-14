# Day 4


# ----> While loop
# ----> Break using while loop
#eg:1
#1.) iterate ffrom 20 to 30 and break the loop in 27
#i=20               |
#while i<30:        | 
 #   if i==27:      |--->method 1
  #      break      |
   # print(i)       |
    #i+=1           |

#Eg:2

#i=20
#while i<31:
 #   print(i)
  #  if i==27:
   #     break
    #i+=1
   
#Eg:3
    
#i=20
#while i<31:
 #   print(i)
  #  i+=1
   # if i==27:
    #    break

   
#Eg: 4

#i=20
#while i<31:
 #   if i==27:
  #      print(i)
   #     break
    #i+=1

# ! ----->Continue using while loop
 # Eg: 5


 
#i=20
#while i<31:
 #   if i==27:
  #    continue
   # print(i)
    #i=i+1

#To print 20 to 31 except 27

#i=20
#while i<31:
 #   i=i+1
  #  if i==27:
   #     continue
    #print(i)

#Eg : 6
   
# While to iterte from 12 to 22
#Find the sum of all numbers

#i=12
#sum=0
#while i<23:
 #   sum=sum+i
  #  i+=1
#print(sum)

#Eg:7

#i=1
#sum=0
#while i<4:
 #   sum=sum+i
  #  i+=1
#print(sum)


#Eg: 8
#Find the avearge of values from 25 to 25

#i=20
#sum=0
#while i<=25:
 #   sum=sum+i
  #  i=i+1
#print(sum/6)

#Eg: 9

#i=20
#sum=0
#count=0
#while i<=25:
 #   sum=sum+i
  #  count+=1
   # i+=1
#print(count)
#print(sum/count)


# ! --->Nested for loop
# Eg: 1

#for row in range(1, 3+1):
 #   for col in range(1, 4+1):
  #      print(row, col)
        
#Eg: 2

# * * * *
# * * * *
# * * * *
# * * * *

#for row in range(4):
 #   for col in range(4):
  #      print("*", end="   ")
   # print()


#rows=int(input("Enter the rows: "))
#cols=int(input("Enter the cols: "))

#for row in range(rows):
 #  for col in range(cols):
  #      print("*", end="     ")
   # print()



#for row in range(5):
 #   for col in range(5):
  # print(row, end="")
  #print()

#sum=0
#for row in range(5):
 #   for col in range(5):
  #      sum=sum+1
   #     print(sum, end="  ")
    #print()


# To print stars in right angled triangle

#for row in range(0, 6):
#    for col in range(0, row):
 #       print("*", end=" ")
  #  print()

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#for row in range(0, 6):
 #   for col in range(row, 6):
  #      print("*", end=" ")
   # print()


# * * * * *
# *       *
# *       *
# *       *
# * * * * *

#for row in range(5):
 #   for col in range(5):
  #      if col==0 or col==5-1 or row==0 or row==5-1:
   #         print("*", end=" ")
    #    else:
     #       print(" ",end=" ")
    #print()



#       *
#      * * 
#     * * *
#    * * * *
#   * * * * *


#for row in range(0, 5):
 #   for col in range(0, 6):
  #      if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
   #         print("*", end=" ")
    #    else:
     #       print(" ", end=" ")
    #print()


#  0 1 2 3 4 5  
#0 *
#1 *  *
#2 *    *
#3 *      *
#4 *        *
#5 * * * * * *

#for row in range(0, 5):
 #   for col in range(0, ):
  #      if ((row==0 and col==5) or (row==



# ---> Data types
#Primary


# Number ----> int, float, complex
# String
# Boolen
# None

# Collection
# List
# tuple
# set
# dictionary


# List
#--> Collection of heterogeneous elements
#1.) If the collection of elements are surrounded by square brackets, it is considered to be list
#Eg:
  # l1=[4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characterstics of list
#1.) List have to be surrounded by[]
#2.) It is mutable (the element in the list are changable)
#3.) Every element inside list is indexed
#4.) The elements inside list will be ordered format
#5.) It can hold duplicate values
#6.) It is heterogenius


# TO acces the elemets in list
#lst1=[1, 4, 1, 7, 89.7, 7.5, "p", "i"]
#print(l1)

#--->Indexing
# In the collection datatypes like list, tuplle, string, the elements will be alloted with predefines unique value called index value


# We have 2 types of indexing
# Positive indexing---> Starts with 0 from left hand side
# Negative indexing---> Starts with -1 from right hand side

#positive indexing

#lst1=[1, 4, 1, 7, 89.7, 7.5, "p", "i"]
#print(lst1[0])
#print(lst1[4])
#print(lst1[20])--> Error

#Negative indexing
#lst1=[1, 4, 1, 7, 89.7, 7.5, "p", "i"]
#print(lst1[-1])
#print([-5])

#---> slicing
lst1=[1, 4, 1, 7, 89.7, 7.5, "p", "i"]
#lst1[start_index:end_index:step]

#print(lst1[0:4])
#print(lst1[6:8])
#print(lst1[3:6])
#print(lst1[:5])
#print(lst1[3:])
#print(lst1[:])

#print(lst1[0:7:1])# --->lst1[0:7]--->both are same
#print(lst1[0:7:2])



# trial =int(input())

#lst1=[1, 4, 1, 7, 89.7, 7.5, "p", "i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4])----> ans:[]
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])

# To insert or add element inside list
#append()
#l1=[9, 8, 0, 6]
#l1.append("car")
#print(l1)


#n = int(input("Enter the number of inputs: "))
#fpr n in range(0, n):
 #   a, b =list(map(int, input(),split()))
  #  print(a, b)




#s1 ="Hello world to all"













    
