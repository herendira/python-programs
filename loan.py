"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: Program to determine whether to loan money based on the following rules. .

"""

print()
print('"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
print('"                          IS THIS A LOAN FOR YOU?                            "')
print('"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
print()
print()

print("Answer the following questions from 1 to 10, 1 means less, 10 means more")
print()
loan=float(input("How large is the loan that you need? "))

good=int(input("How good is your credit history? "))

income=int(input("How high is your income? "))

down_pay=int(input("How large is your down payment? "))

if (loan>=5 and loan<11) and (good>=7 and good<11) and (income>=7 and income<11):
    print("YES! you are elegible for our LOAN")

elif ((good>=7 and good<11)  or (income>=7 and income<11)) and (down_pay>=5 and down_pay<11):
      print("YES! You are elegible for our LOAN ")

elif (good<=7 and good<11) and (income<=7 and income<11):
    print("We are so sorry, but you are not elegible for our LOAN")

elif good<=4:
    print("Our desicion is not" )  
elif income<=4 or down_pay<=7:
    print("Our desicion is YES! you are eligible ")

else:
    print("We cannot help you, look for another LOAN")




