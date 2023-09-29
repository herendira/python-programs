"""
# File: wind.py
# Author: Herendira Gomez
# Class: CSE111 Programming Building Blocks
# Assignment purpose: FUNCTIONS

"""
import math


def wind_formula():
    wind_speed=(i**0.16)
    wind=35.74+(0.6215*temp)-(35.75*wind_speed)+(0.4275*temp)*wind_speed
    return wind
      
def faren():
    temp=celcius*(9/5)+32
    
    return temp

temper=float(input("What is the temperature?: "))
cel_or_fa=input("Fahrenheit or Celsius (F/C)? ")

if cel_or_fa.upper()=="C":
    celcius=temper
    temp=faren()

    for i in range(5,61,5):
        windy=wind_formula()
        print(f"At temperature {temp:.1f}F, and wind speed {i} mph, the windchill is: {windy:.2f} F")    
  
if cel_or_fa.upper()=="F":
    temp=temper
    for i in range(5,61,5):
        windy=wind_formula()
        print(f"At temperature {temp:.1f} F, and wind speed {i} mph, the windchill is: {windy:.2f} F")    




