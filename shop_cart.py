"""
# File: shop_cart.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:09 Milestone (lists)

"""
print("                                          WELCOME TO AMAZIN                                 ")
print("                                         everything is in here                                 ")
print()
print()
items=[]
prices=[]
item=None

print("Please select one of the following: ")
print("1. Add item")
print("2. View cart ")
print("3. Remove item ")
print("4. Compute total ")
print("5. Quit ")
loop=True
while loop:
 print("Please enter an action: ")
 option=input()
 if option=="1":
  price=0
  while item!="quit":
   item=input("What item would you like to add?, enter quit to finish ")
   if item!="quit":
    price=input(f"What is the price of: {item.upper()} $")
    items.append(item)
    prices.append(price)
    print(f"{item.upper()} has been added to the cart. ")      

 elif option=="2":
  print("The contents of the shopping cart are:")
  for i in range(len(items)):
     print(f"{i+1}.{items[i]} - ${prices[i]}")


 elif option=="3":
  print("What item number would you like to remove? ")
  index=int(input())
  items.pop(index-1)
  prices.pop(index-1)
  
  print("The contents of the new shopping cart are: ")
  for i in range(len(items)):
     print(f"{i+1}.{items[i]} - ${prices[i]}") 

 elif option=="4": 
  
  total=0
  tax=0
  all_total=0
  for j in range(len(prices)):
    total+=float(prices[j])
  tax=total*0.30
  all_total=total+tax 

  print(f"The total price of the items in the shopping cart is: ${total:.2f}")
  print(f"The tax of your purchase is: ${tax:.2f}")
  print(f"The total amount after tax is: ${all_total:.2f}")

 elif option=="5":
  print("Thanks for shopping with us")  
  loop=False

 else:
  print("option no valida")                
