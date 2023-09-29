"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  "for" practice,
"""
m=""
word="Commitment"
fav_letter=input("What is your favorite letter? ")
for i, letter in enumerate(word):
    if letter.upper()==fav_letter.upper():
     print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

word="Commitment"
fav_letter=input("What is your favorite letter? ")
for i, letter in enumerate(word):
    if letter.upper()==fav_letter.upper():
     print("_", end="")
    else:
        print(letter.lower(), end="")

print()

phrase="In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
option="YES"

while option.upper()=='YES':
 number=int(input("Write a number: "))
 for i, letter in enumerate(phrase):
   if i % number==0:
    print(letter.upper(), end="")
   else:
    print(letter, end="")

 print()     

 option=input("Do you want to continue? ")
print("BYE!")   

    