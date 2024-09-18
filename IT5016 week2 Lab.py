'''
Software Development Fundamentals Week 2 Lab
Author: Muhammad Moiz Farooq / 20240779
WhiteCliffe College, AKL
''' 
import math

Name=str(input("enter your name:"))
yearofbirth=int(input("enter your year of birth in (YYYY):"))
currentyear=int(input("enter the current year in (YYYY):"))
age=currentyear-yearofbirth
print("Congratulations %s you are %s years old now" % (Name,age))



a = 42
b = 3.14
c = "Hello, World!"
d = [1, 2, 3]
e = (1, 2, 3)
f = {"name": "John", "age": 30}
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
exponentialvalue=math.exp(b)
print("exponential value of b is",b)
modulusofaandb=a%b
print(modulusofaandb)
a+=5
print(a)
a-=10
print(a)
a*=2
print(a)
a/=7
print(a)
upp=c.upper()
print(upp)

b="3.14"
print(type(b))
a="42"
print(a+""+b)
