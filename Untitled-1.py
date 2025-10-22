#python Basics
from math import floor, ceil
# variables 
x = 5 
y = "sai"
x = float (5)
print (type(x))
print(type(y))

x , y , z = ["apple", "banana","cherry"]
print(x)
print(y)
print(z)
x=y=z ="orange"
print(x)

# strings 
h = "hello"
print(h[2])
for x in "hello":
         print(x)

# slicing 
print(h[ :4])
print(h[2 :4])
print(h[ :-1])

# string methods 
print(f"hello my age is {22}")
s = " sai "
print(s.swapcase())
print(s.swapcase())
print(s.title())
print(s.strip())
a = "sai"
b = "chandana"
c = a + b 
print(c)
print(c.count("a"))
print(c.replace("a","i"))
print(c.replace("i","a"))
d = "sai ,jampala "
print (d.split(","))


# numbers 
a = 10 
print(type(a))
b = 2.2
print(abs(2.2))
print(floor(2.2))
print(ceil(2.2))

import random as rd 
a = rd.randint(1,10)

#boolean 
print(bool(None))
print(bool(0))
print(bool(False))
print(bool({}))
print(bool([]))
print(bool(()))
print(bool(""))

# we use for loop 7 while  for looping  (those are 2 primitive loops in python )
for x in range(10):
    print(x)

i = 0
while i < 10:
    print(i)
    i += 1

# if or switch statment is used when we need to check some thing is present or not 
x - 7
if x >5:
      print("yes")

# fucntions 
def sai(a,b):
      return a +b 
print(sai("sai","chandana"))