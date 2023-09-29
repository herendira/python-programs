"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  for, index,
"""

print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
print('"                                                                                                            "')
print('                                      COME AND GUESS THE WORD                                                "')
print('"                                                                                                            "')
print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')

print('Welcome to the word guessing game!')
print()

secret_word = "car"
count = 0
guess = None

print("Your hint is: ", end=" ")
for char in secret_word:
    print("_", end=" ")
print()

while guess != secret_word:
    guess = input("What is your guess? ").lower()
    count += 1

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same "
              "number of letters as the secret word.")
        continue

    for index, char in enumerate(guess):
        if char == secret_word[index]:
            print(f'{char.upper()}', end=' ')
        elif char in secret_word:
            print(f'{char.lower()}', end=' ')
        else:
            print('_', end=' ')
    print()

print('Congratulations! You guessed it!')
print(f'It took you {count} guesses.')