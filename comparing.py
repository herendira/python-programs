"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: Comparing numbers and strings

"""
#Asking 1 part
num1=input("What is the first number? ")
num2=input("What is the second number? ")

#IF else part
if num1>num2:
    print("The first number is greater ")
    print("The numbers are not equal")
    print("The second number is not greater")
    print()
elif num1<num2:
    print("The first number is not greater")
    print("The numbers are not equal")
    print("The second number is  greater")
    print()
else: 
    print("The first number is not greater")
    print("The numbers are equal")
    print("The second number is not greater")
    print()

#Asking part 2
animal=input("What is your favorite animal? ")


#if part2
if animal.lower()=='lion':
    print("That is my favotite animal too")
else:
    print(f"The {animal} is not my favorite animal")



