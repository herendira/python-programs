"""
# File: human_resso.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: open files iterat with them

"""





# with open ("books.txt") as books:
#    for line in books:
#     out_space=line.strip()
    
#     print(out_space)

with open ("hr_system.txt") as system:
   for lines in system:
    out_space=lines.strip()
    print(out_space)
print()
print()

with open ("hr_system.txt") as system:
   for lines in system:
     out_space=lines.strip()
     names=out_space.split()
     name=names[0]
     title=names[2]
     print(f"Name: {name}, Title: {title}")

print()
print()

with open ("hr_system.txt") as system:
   for lines in system:
     out_space=lines.strip()
     names=out_space.split()
     name=names[0]
     number=names[1]
     title=names[2]
     salary=float(names[3])

     print(f"{name}, (ID: {number}), {title} - ${salary:.2f}")

print()
print()

with open ("hr_system.txt") as system:
   for lines in system:
     out_space=lines.strip()
     names=out_space.split()
     name=names[0]
     number=names[1]
     title=names[2]
     salary=float(names[3])
     paycheck=(salary/12)/2

     print(f"{name}, (ID: {number}), {title} - ${paycheck:.2f}")

print()
print()
with open ("hr_system.txt") as system:
   for lines in system:
     out_space=lines.strip()
     names=out_space.split()
     name=names[0]
     number=names[1]
     title=names[2]
     salary=float(names[3])
     paycheck=(salary/12)/2

     if title=="Engineer":
       paycheck=paycheck+1000

     print(f"{name}, (ID: {number}), {title} - ${paycheck:.2f}")








 
