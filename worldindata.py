"""
# File: worldindata.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: open files iterat with them

"""
lowest=28
hihgest=80
with open ("data.txt") as system:
     for lines in system:
         out_space=lines.strip()
         info=out_space.split(",")
         entity=info[0]
         anne=info[1]
         life_exp=info[2]
         # for lines in anne: 
         #  parts=anne.strip() 
         #  year=parts.split()
         #  years=year[3]
         #  code=year[4]

         #  print(years)
         #  print(code)
         print(life_exp)
         #print(anne)
         #print(entity)
        

#          if life_exp <= lowest:      
#           print(f"{life_exp} years. The country that has the lowest life expentacy is: {entity}, in: {anne}")

#           if life_exp >= hihgest:
#                 print(f"{life_exp} years. The country that has the highest life expectancy in the dataset is: {entity}")
          
# print()
               
         
 #print()

# What is the year and country that has the lowest life expectancy in the dataset?


# with open ("data.txt") as system:
#    for lines in system:
#          out_space=lines.strip()
#          info=out_space.split()
#          entity=info[0]
#          anne=info[1]
#          life_exp=float(info[2])
#          if life_exp >= hihgest:
#                 print(f"{life_exp} years. The country that has the highest life expectancy in the dataset is: {entity}")
# # print()

# #What is the year and country that has the highest life expectancy in the dataset?
# print()
# print()
# with open ("data.txt") as system:
#    for lines in system:
#      out_space=lines.strip()
#      info=out_space.split(",")
#      entity=info[0]
#      code=info[1]
#      anne=info[2]
#      life_exp=info[3]

#      if life_exp==86.751:
       
#       print(f"The country that has the highest life expectancy in the dataset is: {entity.upper()}")

# print()
# print()
