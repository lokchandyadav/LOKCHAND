

  # Day 5

# ! commo functions of list

#l1=[6, 7, 8, 9, 0,]
#print(len(l1))
#print(max(l1))
#print(min(l1))

#l1[6, 8, 9, "p", "u"]
#print(max(l1))  #---->error coz its a combination of int and and string
#print(min(l1))  #---->error coz its a combination of int and and string

#l1 =[6,, 7, 8, 9, 0, 8.89, -5, 0.78,]
#print(min(l1))
#print(max(l1))

#l1 =[6, 7, 8, 9, 0, 8.89, -5, 0.78,]
# index()---> to get index value of specific element
#print(l1.index(9))

#l1 =[6, 7, 8, 9, 0, 8.89, -5, 0.78,]
# count()---> how many num of times an element is repeated
#print(l1.count(6))


#l1 =[6, 7, 8, 9, 0, 8.89, -5, 0.78, 8]
#print(l1.count(8))


# ! some functions which is specially used for list

# To add element list
# insert(index_value,element)---> to add element at specific index position

#l1 =[6, 7, 8, 9, 0, 8.89, -5, 0.78,]
#l1.insert(2, "cars")
#print(l1)

#l1 =[6, 7, 8, 9, 0, 8.89, -5, 0.78,]
#l1.insert(6, "bus")
#print(l1)


# To deelete element from the list

#l1 =[6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78,]
#pop--->last element will be deleted
#l1.pop()
#print(l1)



#pop(index_value)--> used to delete element at specific index
#l1.pop(4) # 4 is index value
#print(l1)


# remove(element)----> used to delete element directly
#l1 =[6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78,]
#l1.remove(8.89)
#print(l1)


# del--> to delete the list
#l1 =[6, 6, 6, 7, 8, 9, 0, 8.89, -5, 0.78,]
#del l1 # or del(l1)
#print(l1)


# ? ---> join 2 lists

#l1=[9,0,8]
#l2=["p","o","t",34]
#print(l1+l2)

#or
# extend()--->to combine 2 lists
#l1.extend(l2)
#print(l1)


# ? copy
#l1=[6, 7, 8, 9, 3]
#l2=l1.copy()
#print(l2)
#print(l1)
#print(id(l1))
#print(id(l2))


# ! diff between shallow copy and deep copy
#shollow copy
#import copy
#l1=[8, 9, 0,[5, 6, ], [3, 2, 1]]
#l2=copy.copy(l1)
#l1.append(89)
#print(l1)
#print(l2)

# * deep copy

#import copy
#l1=[8, 9, 0,[5, 6, ], [3, 2, 1]]
#print(l1[-1][1]) --> to index nsted list
#l2= copy.copy(l1)
#l1[-1].append('cars')
#print(l1)
#print(l2)


#import copy
#l1=[8, 9, 0,[5, 6, ], [3, 2, 1]]
#print(l1[-1][1]) --> to index nsted list
#l2= copy.deepcopy(l1)
#l1[-1].append('cars')
#print(l1)
#print(l2)


# ? sort-->arrange elements in list in ascending or descending order
#l1=[9, 7, 45, 0, -6, 5, 12]
#l1.sort() # to arrange in ascending order
#print(l1)

#l1.sort(reverse=True)# to arrange descending order
#print(l1)


#l1=['z', 'i', 'o', 'p']
#l1.sort()
#print(l1)


#l1=['z', 'i', 'o', 'p', 9]# it will get error
#l1.sort()
#print(l1)



# list constructor

#list()--> to conver collection datatype to list

#l3=((8, 9, 0))
#print(list(l3))


#l4=(8, 9)
#print(list((l4)))


#---> nested list

#l1= [8, 9, [0, 8, 7], ['p', 'o', 'y'], [8, 't']]
#print(l1[-2][1])

#print(l1[1:4])
#print(l1[1:-1])


# ? to delete 't' from l1

#l1= [8, 9, [0, 8, 7], ['p', 'o', 'y'], [8, 't']]
#l1[-1].remove('t')
#print(l1)



# / Combine these ["p", "o", "y"],[8,"t'] lists in l1 to ["p", "o", "y", 8, "t']

#l1=["p", "o", "y"]#---> method 1
#l2=[8,"t"]
#print(l1+l2)

#l1[-2].extend(l2)

#print(l1)


# ! ----> Tuple
# char of tuple


#1.) Tuple has to be surrounded by()
#2.) The elements inside tuple are not changeble
#3.) The elements inside tuple are indexed
#4.) The element will execute in order
#5.) It ia heterogeneous
#6.) It allow duplicate elements

# EG:
#t1= (8, 8, 9, 6, 5.78, [9, 0], (6, 8). "hey", 9+6j)
#print(t1)
#print(type9t1))

# ? indexing slicing are all same as list

#l1 = (8)
#print(type(l1)) #int

#l1 = (8,)
#print(type(l1))# tuple


#t1 = 8
#print(type(t1)) # int


#t1 = 8,9
#print(type(t1)) #tuple

#len(), min(), max(), index(), count(), ----> all same as list

# to add element inside tuple ---> cannot add

# cannot delete any element from tuple

# join 2 tuples

#t1 = (8, 9, 0)
#t2 = (6, 7, 8)
#print(t1+t2)


# to add all elements inside list and tuple

#sum()
#l1 = (8, 9, 7, 6)
#print(sum(l1))

# * sort tuple

#t1 = (8, 9, 0, 89, 12)
#print(tuple(sorted(t1))) # dessending order

#t1 = (8, 9, 0, 89, 12)
#print(tuple(sorted(t1, reverse=True))) # assending order


# * Iterate list and tuples

#l1=[9, 8, 0, 6, 5]
#for i in l1:
 #print(i)

# Iterate based on index value
#l1 = [9, 8, 0, 6, 5]
#for i in range(0, 5):
 #   print(i)


#l1 = [9, 8, 0, 6, 5]
#print(l1[0])


#l1 = [9, 8, 0, 6, 5, 8, 56]
#for i in range(0,len(l1)):
 #   print(l1[i])


# indexing and slicing----> same as list and tuple

#s1 = "hello world"
# * to access string
#print(s1)
#print(s1[0:5])


#----> len(),min(),max(),index(),count()...

#s1 = "hello world"
#print(len(s1))
#print(min(s1))
#print(max(s1))

#ord()--> used to find the ASCII value of a character
#s1 = 'u'
#print(ord(s1))

# functions of string
#s1 = "hello world"
# ? to convert all characters to upper case
#print(s1.upper())

# ? to convert all characters to lower case

#s2 = "HELLO WORLD"
#print(s1.lower())


# strip()---> to eliminate the space in beginning and end of string


#s1 = "    Where are you? "
#print(s1.lstrip())    #lstrip is used to remove the starting spaces

#s1 = "where are you?          "
#print(s1.rstrip())      # rstrip is used to remove the ending spaces


#s1 = ' Where are you '
#print(s1.strip())


# split function---> to split the words in string based on a character

#s1 = "where are you?"
#print(s1.split(" "))
#print(s1.split("r"))

#print(s1.split("re"))



# replace()---> to replace a specific character in the string

#s1 = "where are you"
#print(s1.replace('r','&&'))


# swapcase()----> to convert capital to small and small to capital at a time
#s1 = "Hey there"
#print(s1.swapcase())


# title()---> to write the string in format of title
#s1 = 'never give up '
#print(s1.title())

# capitalize()---> 1st char of string will be converted to capital
#s1 = 'never give up'
#print(s1.capitalize())

# join the strings'
#s1 = "hello"
#s2 = "world"
#print(s1+s2)


#s1 = ''how are you
#i am fine
#hey there


#splitlines function---> used to split the string based on lines

#print(s1.splitlines())

# find ()
#s1 = "hello world"
#print(s1.find('h'))
#print(s1.index('e'))

#join()---->
#l1 = ['hey','there']
#print(" ".join(l1))
#print("$".join(l1))


#s1 = "welcome to all"
#print(s1.endswith('l'))
#print(s1.startswith('w'))

#s1="67"
#print(type(s1))
#print(s1.isdigit())


# print the string in reverse manner

#s1 = "welcome to all"
#s1_reversed=s1[::-1]
#print(s1_reversed)

#print(s1[::-1])


#Eg---> Eg:1
# wap to find the number of lower case letters

#s1 = "HEY there you aRE"
#print(s1.lower())

#s1 = "HEY there you aRE"
#count = 0
#for i in s1:
 #   if i.islower():
  #      count+=1
#print("The total num of lower case letters are: ",count)


# ! ---->Eg:2
#s1= 'restarter'
#fst = s1[0]
#bal =s1[1:]
#txt =bal.replace(fst,"$")
#print(fst+txt)

#str1 = "bbbbbbyyyybbbaaioo"
#str2 = "%"

# ! --->Eg:3

s1 = '''Lorem Ipsum is simply dummy text of the printing and
typesetting industry. Lorem Ipsum has been the industry's
standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type
specimen book. It has survived not only five centuries, but also
the leap into electronic typesetting, remaining essentially
unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more
recently with desktop publishing software like Aldus PageMaker
including versions of Lorem Ipsum.'''

#characters = len(s1)
#print(characters)

#words = s1.split(" ")
#print(len(words))


#sentences = s1.split(" ")
#for val in sentences:
 #   if val=='':
  #      index = sentences.index('')
   #     sentences.pop(index)
#print(len(sentences))

#space=0
#for val in s1:
 #   if val ==" ":
  #      space=space+1
#print(space)




#1.) Python program to capitalize the first and last character of  
# each word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]










































