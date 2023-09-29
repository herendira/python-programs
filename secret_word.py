"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Secret Word
"""


print()
print()
print('                                 WELCOME TO THE WORD GUESSING GAME                                           ')
print()
print()



counting=0
word='nabucodonosor'
hint=''

print("your hint is ")
for hint in word:
      print("*", end=" ")

word1=str(input("\n What is your guess? "))
counting=counting+1


while word!=word1.lower():
    print("Your guess was not correct ")
    word1=str(input("What is your guess? "))
    counting=counting+1

print("Congratulations! You guessed it!") 
print(f"It took you {counting} times")   
