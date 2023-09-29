"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:LISTAS
"""
friends=[]
name=''


print("Write END to finish your list of friends")

while name!='end':
    name=input("Type the name of a friends: ")
    if name!='end':
     friends.append(name)
print()
print("Your friends are: ")    

for n in friends:
    print(n)
    




