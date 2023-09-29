"""
# File: shopping_cart.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:LISTAS ANIDADAS OF NUMBERS
                    AND LETTERS
"""
print()
print("                           WELCOME TO GROSERIES .COM                                  ")
print()
print()


#variables
item_list=[]
item=''
prices=[]
price=0
total=0
option=''

#menu

print("Add item option [1]")
print("See my shopping list option [2]")
print("Exit option [0]")


option=int(input("What is your number option? "))

while option!=0:

 if option==1:

   while True:
    item=input("What item do you like to add, (enter f two times to finish): ")
    

    if item.lower()=="f":
        
      breakpoint
      
    else:
   
      price=float(input(f"What is the price of {item}: $ "))
      prices.append(price)
      item_list.append(item)
      print(f"{item} has been added to the cart")
      print()
  
  # option=input("Enter your option from the menu: ")
 

         
 #elif option==2:

print("--------This is your shopping cart---------")
print()
for n in prices:
    total=total+price

    for i in item_list:
       print(i, end=" ") 
print(i)
print(f"Your total is: ${total:.2f}") 
 

# else: ("Invalid option")
print()

#option=input("Enter your option from the menu: ")
 

print()
print("thanks for shoppinf in GROSERIES.COM")             
         
       
        






