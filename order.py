"""
# File: order.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: Use of variables and expressions for straight-forward math calculations

"""
print("                      WELCOME TO RESTO CHEZ MICHEAL")
print()
print("           We are ready to take your order, please follow the questions below")
print()
name= str(input("What is your name: "))

 #Asking quantities part
child_meal=float(input("What is the price of a child's meal? $"))
adult_meal=float(input("What is the price of an adult'smeal? $"))
tot_child=int(input("How many children are there: "))
tot_adult=int(input("How many adults are there?: ")) 
soda=int(input("How many drinks do you want?: "))
appet=int(input("How many appetizers dou you want?: "))
tax_rate=float(input("What is the sales tax rate?: "))

#Calculating part
sub_child=child_meal*tot_child
sub_adults=adult_meal*tot_adult
sub_sodas=float(soda*1.75)
appets=float(appet*1.97)
sub_tot=float(sub_child+sub_adults+sub_sodas+appets)
sale_tax=sub_tot*(tax_rate/100)
total=sub_tot+sale_tax

subtotal="{:.2f}".format(sub_tot)
salestax="{:.2f}".format(sale_tax)
totals="{:.2f}".format(total)



#Displaying part
print("\n\n")
print(f"Subtotal: $ {subtotal}")
print(f"Sales Tax: $ {salestax}")
print(f"Total: $ {totals}")
print("\n\n")

#Asking quantities part 2
pay_amount=float(input("What is the payment amount?: "))
tip1=pay_amount*0.15
tip="{:.2f}".format(tip1)
#Calculating part 2
change=pay_amount-total
tot_change="{:.2f}".format(change)


#Displaying part 2
print(f"Change: $ {tot_change}")
print()
print(f"Don't forget $ {tip} the tip")
print()
print(f"      THANKS {name.upper()} FOR VISITING US!!")
















