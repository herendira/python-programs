wind_speed=0


velocity=0
celcius=0
farenheit=0

def wind_formula():
    
    wind_speed=(i**0.16)
    wind=35.74+(0.6215*temp)-(35.75*wind_speed)+(0.4275*temp)*wind_speed
    print(wind)
    
def faren():

    temp=celcius*(9/5)+32
    print(temp)
    

temp=float(input("What is the temperature?: "))
for i in range(5,61,5):


   wind_formula()


