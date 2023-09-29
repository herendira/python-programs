"""
# File: shopping_list.py
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


print("Please enter the items of the shopping list (type: quit to finish)")
while item!="quite":
    if item=="quite":
        break
    else:
        item=input("Item: ")
        items_list.append(item)

items_list.pop()
        
print()
#displaying shopping list
print("The contents of the shopping cart are: ")
for n in  items_list:
    print(n)
print()

#displaying shopping list with index

for i in range(len(items_list)):
    item=items_list[i]
   
    print(f"{i}.{item}")
print()

#change item
index=int(input("Which item would you like to change? "))
new_item=input("What is the new item? ")
items_list[index]=new_item




#printing the new list
print("The shopping list with indexes is: ")
for i in range(len(items_list)):
    item=items_list[i]
   
    print(f"{i}.{item}")

# First prepare the list, just like the previous checkpoint    

# print("Please enter the items of the shopping list (type: quit to finish):")

# shopping_list = []
# item = None

# while item != "quit":
#     item = input("Item: ")

#     if item != "quit":
#         shopping_list.append(item)


