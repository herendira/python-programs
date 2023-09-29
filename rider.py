"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Program for knowing if the person could ride or not.

"""
age1=int(input("What is the age of the first rider? "))
height1=int(input("What is the height of the first rider? "))
weight1=int(input("What is the weight of the first rider"))
second_rider=str(input("Is there a second rider (yes/no)? "))

permite=False
if second_rider.upper()=="YES":
    #permite=True
    age2=int(input("What is the age of the second rider? "))
    height2=int(input("What is the height of the second rider? "))
    weight2=int(input("What is the weight of the second rider" ))
else:
   second_rider.upper()=="NOT"
   #permite=
if (age1>=12) and (weight1>=62) and (height1>=36):
      permite=True

elif (age1<18 and age1>=12) or (age2<=18 and age2>=12) and (height1>=52 and height2>=52):
       passport=str(input("Do you have a Golden Passport? YES or NOT? "))
       if passport.upper()=="YES":
          permite=True
       else:
        permite=False
#else:
    #permite=False


if permite==True:
 print("Welcome to the ride. Please be safe and have fun! ")
 print("FIN")

else:
    permite==False
    print("Sorry dude, yo cannot ride with us ")
    print("FIN")
