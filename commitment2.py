"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  "for" practice,
"""


print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
print('"                                                                                                            "')
print('                                      COME AND GUESS THE WORD                                                "')
print('"                                                                                                            "')
print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')

word='moroni'
counting=0
guess=''
hint='_ ' * len(word)
option='YES'
while option.upper()=='YES':
   while guess != word:
    print(f"Your hint is {hint} ")
    guess=input("What is your guess? ")
    counting=counting+1
    if len(word)!= len(guess):
       print("Your guessing word must have the same numbers of lettres, ")
    elif guess != word:
        hint=''
        for index in range (len(guess)):
            #print(f"{index} {guess[index]} {guess} {word[index]} {word} ")
            if guess[index] ==(word[index]):
                hint=f'{hint}{guess[index].upper()} '
                print("MATCH ")
            elif(guess[index]) in word:
                hint=f'{hint}{guess[index].lower()} '
                print("Present ")
            else:
                hint=f'{hint}_'
                print("No Match ") 
    print("Try again ")

    print("Congratulation!! You guessed it ")  
    print(f'It took you {counting} times ') 

option=("Do you want to continue? YES or NOT")

print('BYE ')


