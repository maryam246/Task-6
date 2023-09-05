# Example of for loop(use with sequence list,tuple.e.t.c):
x = [1,"kashmir",33.5]
# here i is variable which take 1 value at a time
for i in  x:
    print(i)
    
# 2nd example:
for h in range(1,18,2):
    print(h,end=",")
print()
# Example of While loop:
i = 1
while(i<5):
    print(1,"Hi")
    i=i+1
    
#2nd example of while:
k = 5
while(k>=1):
    print(k,"Ali")
    k=k-1 # here use decrement
    
# Another example of while:
l = 1
while(l<=5):
    print("ALI ",end="")
    j = 1
    while(j<=3): #here use nested while loop
        print("khan ",end="")
        j+=1
    l+=1
    print()

#Example of Loops and control statements:
# Continue:
s=[1,"maryam",10,5,8]
for n in s:
    if n==5:
        continue
    print(n)
#Break:
u = 1
while(u<=5):
    if u==3:
        break
    print(u, "break")
    u+=1
#Pass:
for i in range(1,5):
    if i==2:
        pass
    else:
        print(i,"by")

# Example of Looping technique in python:

""" Way 1: Using enumerate(): 
print the index along with the value: present in that particlar index."""

for key,value in enumerate(["I","am","a","student"]):
    print(key,value)
    
# way 2: Using zip() function: combine 2 similar containers(list-list or dict-dict).
num = [1,2,3]
num2 = ["ali","nimra" ,"noman"]
for k in zip(num,num2):
    print(k)
    
# another example:
name = ['ALI','KIRAN','AZI']
age = [20,30,40]
for names,ages in zip(name,age):
    print("My name is {0} and i am {1} years old.".format(names,ages))
    
# way 3: Using items():
# iteritems() is renamed to items() in python3
# using items to print the dictionary key-value pair

dic ={1:"aima",2:"fraz"}
print("The key values 1 and 2 contain items is: ")
for i,j in dic.items():
    print(i,j)
# way 4: Using Sorted:
s = [2,45,21,56,98,56,8,4]
print("The sorted list : ")
for i in sorted(s):
    print(i,end=" ")
print()
print("The sorted list as a set no repeated element : ")
for i in sorted(set(s)):
    print(i,end=" ")
    
    
# way 5: Using reversed oder:
r = [3,5,4,3,2,1,2,9,7]
print("The reversed order of r is: ")
for i in reversed(r):
    print(i,end=" ")
    

# Example of range VS Xrange in python:
a = range(1,6) #range()
print(type(a)) #testing type of range()

"""x = xrange(1,6) #xrange()
print(type(x)) #testing type of xrange()"""


a = range(1,6) #slice operation on xrange
print(a[2:4])
"""x = xrange(1,6)
print(x[2:4])"""#slice operation on xrange

#Example of Programs for printing pyramid technique in python:
#Here are some Python programs to print pyramid patterns using nested loops
# 1. Print a Half Pyramid:
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("next pattern")
# 2. Print a inverted-Half Pyramid:
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("next pattern")
# 3. Print a full Pyramid:
for i in range(1,5):
    for s in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("next pattern")
# 4. Print a inverted full Pyramid:
for i in range(4,0,-1):
    for s in range(1,5-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# Example of Chaining comparison in python:
a = 6
print(2<6<8)
              # this  comparision is not a GOOD WAY.
a = 6
print(7<6<8)

# So, we use logical operator to check the Chaining comparison:
a = 6
print(2<6 and 6<8)

a = 6
print(2<6 or 6<5)

a = 6 #Uniary operator
print(not 6<7)

# chaining comparison operators
a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
com1 = a <= b < c > d is not e is f
com2 = a is d > f is not c
print(com1)
print(com2)

# Example of else with for:
for i in range(1,6):
    print(i)
else:               ## Executed because no break in for
    print("hello")
    

"""# Example of switch function:
d={1:"monday",
    2:"tuesday",
    3:"wednesday"
    }
    
n = int(input())
print(n)"""

#Example of Python Itertools:
from itertools import count

for r in count(start=1, step=3):
	if r > 10:
		break
	print(r) 

# Example of Python iter() and next()|converting an object in iterator:
# simply itreror
l = (1,2,3,4,5)
for i in l:
    print(i,end=" ")
    
# iterator with iter() and next:
l =(1,3,5,7)
x =iter(l)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#Example of Generators in Python:
def A():
   n = 1
   while(n<=10):
      sq =n*n
      yield sq
      n+=1
   
values =A()

for i in values:
    print(i)
    
#Example of Generator expression in python:
# use() arround a comprehension to Generator expression:
my_list=[x for x in range(0,19)]
my_generator=(x for x in range(0,19))

print(my_list)
print(my_generator)

#To generat the next item in generator we use nex() function
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

# we can iterate through a generator through a for loop
# remaining items are give:
for k in my_generator:
    print(k)
    
# once all the item is generated ,then generator is exhausted.