"""
# File: find_things.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Open a file and search.
"""
max_years=-1
min_years=99
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

for datas in people:
    clean=datas.split()
    names=clean[0]
    years=int(clean[1])
   

    print(names)
    print(years)   
    


    if years < min_years:
       min_years=years
       min_name=names
       
    if years> max_years:
       max_years=years
       max_name=names  

print(f"The min age is: {min_years} from {min_name}")  
print(f"The max age is: {max_years} from {max_name}") 

