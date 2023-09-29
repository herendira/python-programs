"""
# File: list_numbers.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:LISTAS OF NUMBERS

"""
import math
numberss=[]
number=''
longitud=0
sum=0
average=0
larger_number=0
i=0
print('Write a 0 when you finish your list of numbers ')
while number!=0:
     
     number=int(input("Enter number: "))
   
     numberss.append(number)
    
     

#sum
for n in numberss:
    sum=sum+n
print()
print("The sum is: ", sum)   


 #average   
longitud=len(numberss)  
average=sum/longitud
print()
print(f"The average is:  {average:.2f}") 

#largest number
max_number=None

for number in numberss:
   if (max_number is None or number>max_number):
     max_number=number
print(f"The largest number is {max_number}")   

#number positive and negative
little=0
for number in numberss:
   min(numberss)
   if number>0 and number<max_number:
    little=number
print("the smallest number is: ", little)    

        


#sort thing

numberss.sort()

print("The list for minimum to maximum is: ")
for n in numberss:
    
    print(n)
