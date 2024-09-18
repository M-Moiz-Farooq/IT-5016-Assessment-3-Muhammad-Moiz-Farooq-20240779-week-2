'''
Author: Muhammad Moiz Farooq
IT5016 Software Development Fundamentals
WhiteCliffe College, AKL

'''
Name=str(input("enter your name:"))
yearofbirth=int(input("enter your year of birth in (YYYY):"))
currentyear=int(input("enter the current year in (YYYY):"))
age=currentyear-yearofbirth
print("Congratulations %s you are %s years old now" % (Name,age))
