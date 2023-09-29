"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Loops practice.

"""

number=int(input("Please write a positive number "))
while number<0:
    print("Sorry, that is a negative number. Please try again. ")
    number=int(input("Please write a positive number "))
print(f"The number is: {number}")

ans=str(input("May I have a piece of candy? "))
while ans.upper()=='NO':
    ans=str(input("May I have a piece of candy? "))
if ans.upper()== 'YES':
 print('Thank you my dear ')  
else:
    print("your reponse is incorrect") 

 

    