"""
# File: shopping.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:LISTAS

"""

items=[]
prices=[]
total=0

print()
print("                           WELCOME TO AMAIZING.COM                                  ")
print()
print()


while True:
    item=input('What item would you like to add? (f to finish): ')
    if item.lower()=='f':
        break
    else:
        price=float(input(f"What is the price of {item}: $"))
        print(f"{item.upper()} has been added to the cart")
        items.append(item)
        prices.append(price)

#displaying shopping cart
print()
print("The contents of the shopping cart are: ")
for item in items:
    print(item)

#making the total of the shopping cart
print()
for price in prices:
    total=total+price
print(f"Your total is: ${total:.2f}")

#deleting item
del_item=input("What item of the list do you want to delete? ")
items.remove(item)
print("This is your shopping cart now: ")
for item in items:
    print(item)

#making the total of the new shopping cart
print()
total=0
for price in prices:
    total=+price
print(f"Your new total is: ${total:.2f}")



