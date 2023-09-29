"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Program that determines the letter grade for a course

"""

grade=int(input("What is your grade percentage: "))
if grade>=90:
    lettre="A"
    
elif grade>=80:
    lettre="B"

elif grade>=70:
    lettre="C"
    
elif grade>=60:
    lettre="D"
   
elif grade<60:
    lettre="F"
   

grade2=grade%10
signo=""
if grade2>=7:
   signo="+"
elif grade2<3:
    signo="-"
else: signo=""

print(f"Your letter grade is: {lettre}{signo}")
if grade>=70:
   print("Congratulation!!you passed the cours")
else:
    print("Keep trying") 

   
 
      



