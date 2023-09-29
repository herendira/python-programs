"""
# File: func_area.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: Areas with functions

"""

def area_square():
    lado= float(input("Enter the value of a side: "))
    areasq=lado*4
    print(f"Square Area= {areasq}")
   

def area_rectan():
    altura=float(input("Enter the height: ")) 
    base=float(input("Enter the base: ")) 
    areare=(base*altura)/2
    print(f"The rectangle area is: {areare}") 

def area_cir():
    radio=float(input("Enter the ratio: "))  
    areacir=3.14*(radio*radio) 
    print(f"The area of a circle is: {areacir}") 
 
print("[1] Area of a Square")
print("[2] Area of a Triangle")
print("[3] Area of a Circle")
print("[4] Exit")

loop=True
while loop:
 option=int(input("What is your option "))

 if option==1:
     area_square()
     
 elif option==2:   
    area_rectan()

 elif option==3:
     area_cir()

 elif option==4:
     print("Thanks")
     loop=False

 else:
    print("Option invalide")



