"""
# File: life_expectancy.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose:  Open fil and searching in a huge data base
"""
import math
interes=int(input("Enter the year of interest: \n\n")) 
intere=input("Enter the country of interest: \n\n")
max= -1
min= 9999
long=0
sum=0
average=0

newlife=[]
new_country=[]

with open("life-expectancy.csv") as file:
     next(file) # next(10, file) esto salta la primera linea del file
     for line in file:
         clean = line.strip()
         data = clean.split(',')
         country = data[0]
         year = int(data[2])
         life_expectancy = float(data[3])

         if year == interes: 
          newlife.append(life_expectancy)  

          if (life_expectancy > max):
                   max=life_expectancy
                   countrymax=country
                   yearmax=year
                  
       
          if life_expectancy < min:
                 min=life_expectancy
                 countrymin=country
                 yearmin=year


         if country.lower() == intere.lower():
          newlife.append(life_expectancy)  
          
          if (life_expectancy > max):
                   max=life_expectancy
                   yearmax=year
                 
       
          if life_expectancy < min:
                 min=life_expectancy
                 yearmin=year



long=len(newlife)
#print(long)

for n in newlife:
  sum=sum+n
#print(sum)

average=sum/long
ave=int(average)
#print(ave) 

print(f"\nFor the year {interes} \n\n")

print(f"The average life expectancy across all countries was {ave}\n")

print(f"The max life expectancy is: {int(max)} from {countrymax.upper()} in {yearmax}\n")
           
print(f"The min life expectancy is: {int(min)} from {countrymin.upper()} in {yearmin}\n\n") 

print(f"For: {intere.upper()}, the max life expectancy was: {int(max)} in {yearmax} et the minimun was: {int(min)} in {yearmin}")
             
             


    

              
            
           
      
        