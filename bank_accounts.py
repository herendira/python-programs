"""
# File: bank_accounts.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: Multiple lists

"""
import math
bank_accounts=[]
balances=[]
account=""
balance=0
print("Enter the names and balances of bank accounts (type: quit when done) ")

while account!="quit":
   account=input("What is the name of this account? ")
   if account!="quit":
           balance=float(input("What is the balance? "))

           balances.append(balance)
           bank_accounts.append(account)






#account infor
print()

print("Account Information: ")
total=0
for i in range(len(bank_accounts)):
   print(f"{i}.{bank_accounts[i]} - ${balances[i]}")

 #total   
   total+=balances[i]

print(f"Total: ${total:.2f}")



#average
longitud=0
average=0

print()

average=total/len(balances)
print(f"Average: ${average:.2f}")
print()
#max account
max_number=None
balanc=-1

for balanc in balances:
   if (max_number is None or balanc>max_number):
     max_number=balanc

print(f"The highest balance is ${max_number}")   

max_balance=-1
acc_name=None

for i in range(len(bank_accounts)):
    account=bank_accounts[i]
    balance=balances[i]

    if balance>max_balance:
        max_balance=balance
        acc_name=account
   
print(f"The highest balance: {acc_name} - ${max_number:.2f}")

#update account

option="yes"
option_index=None
new_amount=0

print("Do you want to update an account? ")
option=input()

while option.upper()=="YES":
    
    print("What account index do you want to update? ")
    index=int(input())
    print("What is the new amount? $")
    new_amount=input()
    
    balances[index]=new_amount

    
    print()

    print("Account Information: ")
    
    for i in range(len(bank_accounts)):
     print(f"{i}.{bank_accounts[i]} - ${balances[i]}")

    print("Do you want to update an account? ")
    option=input() 

 


print("Thanks for trust in us your bank")
