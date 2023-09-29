def wind_chill(air_temperature, wind_speed):
    return 35.74 + (0.6215 * air_temperature) - (35.75 * (wind_speed**0.16)) + (0.4275 * air_temperature * (wind_speed**0.16))

def celcius_to_fahrenheit(temperature):
    return temperature * 1.80000 + 32.0

temperature = float(input('What is the temperature? '))
f_or_c = input('Fahrenheit or Celsius (F/C)? ').lower()

if 'c' in f_or_c:
    temperature = celcius_to_fahrenheit(temperature)

for wind_speed in range(5, 65, 5):
    print(f'At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill(temperature, wind_speed):.2f}F')