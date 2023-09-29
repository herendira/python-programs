"""
File: falling.py
Author: Herendira Gomez
Class: CSE111 Programming Building Blocks
Assignment purpose: Determine how fast an object will fall.

"""

import math

#Asking part
print("Welcome to the velocity calculator. Please enter the following:")
mass=float(input("Mass (in kg):"))
gravity=float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time=float(input("Time (in seconds): "))
density=float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
area_cross=float(input("Cross sectional area (in m^2): "))
drag_constant=float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

#Calculating part
c=0.5*density*area_cross*drag_constant
variable1=math.sqrt((mass*gravity)/c)
#raiz=math.sqrt(variable1)
variable2=-1*((math.sqrt(mass*gravity*c)/mass)*time)

variable3=1-math.exp(variable2)
velocity=variable1*variable3



#Displaying part
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after 10.0 seconds is: {velocity:.3f} m/s")
