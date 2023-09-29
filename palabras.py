
word="moroni"
hint=""
lettre=""
counting=0

hint=str(input("What is your guess? "))
counting=counting+1


   


while len(word)!=len(hint) or word!=hint.lower():
 
 for hint in word:
      print("*", end=" ")
 print("\n your word does't work, write another ")
 
 hint=str(input("What is your hint? "))
 counting=counting+1

 
  

print("Congratulations! You guessed it!") 
print(f"It took you {counting} times")   



