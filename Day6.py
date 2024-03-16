#1.) Python program to capitalize the first and last character of  
# each word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]


#str1= input("Enter the string: ")
#fst=str1[0].upper()
#lst=str1[-1].upper()

#print(fst+str1[1:len(str1)-1]+lst)

#n=128
#temp=n
#while n !=0:
 #   rem = n%10
  #  check = temp%rem
   # if check !=0:
    #    str = "No"
     #   break
    #else:
     #   str1 ="Yes"
    
    #n=n/10
#print(str1)


#n = 128
#temp = n
#str1 =""
#while n!=0:
 #   rem = n%10
  #  check= temp% rem
   # if check==0:
    #    f1 = 1

        
     #   n=n/10

#if f1==0:
 #   print("Yes")
#else:
 #   print("NO")

#l1 = [8, 9, 0, 7]
#l2 = [7, 6, 5, 4]
#l3 = []


#print(l1[0]+l2[0],l1[1]+l2[1])

#for val in range(len(l1)):
 #   ans = l1[val]+l2[val]
  #  l3.append(ans)
#print(l3)


# --->SET

# 1.) set can be created using{}
# 2.) the elements inside set are not indexed
# 3.) does not allow duplicate values
# 4.) it unordered
# 5.) heterogeneous---> accept only unmutable datatypes
# 6.) mutable or changable


#Eg:1
#s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5),"truck",'e'}
#print(s1)


# Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2)

#Eg:3
# min(), max(), len()

#Eg:4

# to add element inside set

#s1 = {8, 78, 67, 'u'}
#add()
#s1.add(45)
#print(s1)


#update
#s1.update([9,0])
#print(s1)

# To delete element one element inside set
#s1 = {8, 78, 67, 'u'}


# pop() # to delete one element randomly
#s1.pop()
#print(s1)


# remove()
#s1.remove(78)
#print(s1)

#discard()
#s1.discard(8967)
#print(s1)


#clear()
#l1 = {}
#print(type(l1)))---> data type is dict

#s1 = set() --> to create empty set
#print(type(s1))

#s1 = {8, 9, 0, }
#s1.clear()
#print(s1)

#del s1
 #print(s1)

# join the sets
#s1 = {9, 0, 8}
#s2 = {9.90, "card", 't', 56}
#union ()---> to combine two ssets
#s3 = s1.union(s2)
#print(s3)

#s1 = {4, 5, 6}
#s2 = {5, 6, 7, 8}
#print(s1.intersection(s2))


# difference()
#s1 = {4, 5, 6}
#s2 = {5, 6, 7, 8}
#print(s1.difference(s2))
#print(s2.difference(s1))
#print(s1.symmetric_difference(s2))


# isdisjoit(), issubset(), issuperset()

#s1 = {8, 9, 0}
#s2 = {6, 7, 5, 8, 9, 0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))
#print(s1.isdisjoint(s2))


# Joint set

#s1 = {1, 2, 3, 4, 5}
#s2 = {3, 2,  7, 8, 9}

#for val in s1:
 #   if val in s2:
  #      str1 = "Its a joint function"
#print(str1)


# ------> Dictionaries
#eg:1
#d1 = {1:100,'a':200, 4.5:"hello"}
#marks_std1 = {"English":79,"Maths":20,"physics":60}



#print(d1)
#print(len(d1))

# char of dictionary
#1.) have to be surrounded {}
#2.) It have to be in the form of key, value pair
#3.) It is mutable
#4.) Duplicate keys are not allowed, duplicate values are allowed
#5.) It is unindexed
#6.) It is ordered
#7.) Key does not allow multiple datatypes, values allow multiple datatype


#d1 = {1:100, 2:200, 3:300, 4:400}

# to access elements in dictionary
#print(d1)
#or
#to  access the values
#print(d1[3])
# some common functions
# len(), min(), max()
#print(min(d1))
#print(max(d1))

# To find min, max based on values
#print(min(d1.values()))
#print(max(d1.values()))


# dictionary based functions
# to add elements (key and value pair) in dictionary

#d1 = {1:100, 2:200, 3:300, 4:400}
#d1[5] = 500
#print(d1)


# To replace a value in dictionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#d1[2] = 'mango'
#print(d1)

#delete element from dictionary

#d1 = {1:100, 2:200, 3:300, 4:400}
#popitem()
#d1.popitem()
#print(d1)


#pop
#d1.pop(2) #2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 ditionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple","b":"ball","c":"cat"}
#d1.update(d2)
#print(d1)

# get()
#d1 = {1:100, 2:200, 3:300, 4:400}
#print(d1[90])
#print(d1.get(90))


# to print all the keys
#print(d1.keys())
#print(type(d1.keys()))

#to print the all values
# print(d1.values())

#Iterating dictionary
# for val in d1: # to ietrate keys alone
#print(val):

#for val in d1.values(): # to iterate values alone
#print(val)

#to get both keys and values
#d1 = {1:100, 2:200, 3:300, 4:400}
#for key, val in d1.items():
 #   print(key,val)


# ! problem:1

#n = int(input("Enter the value: "))
#integer = []
#float_value =[]
#string=[]
#for val in range(n):
 #   value = eval(input("Enter the values: "))
  #  if type(value)==int:
   #     integer.append(value)
   # elif type(value)==float:
    #    float_value.append(value)
    #elif type(value)==str:
     #   string.append(value)
    #else:
     #   print("please provide data in int, float_value,string")
#print(integer)
#print(float_value)
#print(string)
        
       
        

#1.)Swap elements in string list
# The original lists is :['Gfg','is','best','for','Geeks']
#LIst after performing character swaps : ['efg', 'is', 'bgst', 'for', 'eGGks']

# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}




#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
#set3 = set()
#for val in set1:
 #   if val not in set2:
  #      set3.add(val)
#for val in set2:
 #   if val not in set1:
  #      set3.add(val)
#print(set3)


#---->problem 3
l1 = [1, 2, 3, 4]
l2 = ["a", "b", "c", "d"]
print(l1+l2)























 
    



    
