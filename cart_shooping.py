"""
# File: cart_shopping.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:LISTAS 

"""
import math
items_list=[]
item=''
price=''
prices=[]
option=''
total=0
print("write f to finish")
while item!="f":
    if item=="f":
        break
    else:
        item=input("What item would you like to add? write f to finish ")
        items_list.append(item)
        price=input(f"What is the price of {item.upper()}: $")
        prices.append(price)
        print(f"{item.upper()} has been added to the cart")

print()

    

#displayin shopping cart
print("The contents of the shopping cart are: ")
for n in  items_list:
    print(n)

print()    

#total of shopping
for n in prices:
    total=total+n
print()
print(f"The TOTAL of your purchase is: $ {sum:.2f}")