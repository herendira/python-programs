"""
File: farenheit.py
Author: Herendira Gomez
Class: CSE111 Programming Building Blocks
Assignment purpose: Program that converts from Fahrenheit to Celsius. Displaying the result to one decimal place of precision.

"""
temp_fahren=float(input("What is the temperature in Fahrenheit? "))
celcius=float(temp_fahren-32)*5/9
print(f"The temperature in Celsius is {celcius:.1f} degrees. ")
