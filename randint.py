"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Random magic number
"""

import random

ans='YES'
counting=0
number1=0

while ans.upper()=='YES':
    number = random.randint(1, 100)
    counting=0
    """print(f"What is the magic number? {number} ")"""
    while number>number1 or number<number1:
        number1=int(input("What is your guess? "))
        counting=counting+1
        if number1>number:
         print("Lower ")
        else:
         number1<number
         print("Higher ")


    print("You guessed it!")
    print(f"You tried {counting} times")

    ans=str(input("Do you want to play again? YES or NOT "))

if ans=='NOT':
 print("thanks for playing with me ")



    