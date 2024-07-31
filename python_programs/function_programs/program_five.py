'''
5. Write a program WindChill.py that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be:

Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
than 120 or less than 3 (you may assume that the values you get are in that range).
'''
def calculate_wind_chill(temp_f, wind_speed_mph):
    
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275
    
    wind_chill = (a + b * temp_f - c * (wind_speed_mph ** 0.16) + d * temp_f * (wind_speed_mph ** 0.16))
    return wind_chill


temperature = float(input("enter the input in fahrenheit:"))
wind_speed =float(input("enter the input in miles per hour:"))

wind_chill = calculate_wind_chill(temperature, wind_speed)
print(f"The wind chill index is: {wind_chill}°F")

