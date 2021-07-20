def celsius_to_fahrenheit(c):
    fahrenheit = (c * (9/5)) + 32   #Formula for calculating temperature in Fahrenheit
    return fahrenheit

def fahrenheit_to_celsius(f):
    celsius = (f - 32) * (5/9)   #Formula for calculating temperature in celsius
    return celsius


c = 80
f = 80
print(f"The temperature from celsius to Fahrenheit is {celsius_to_fahrenheit(c)}")
print(f"The temperature from Fahrenheit to Celsius is {fahrenheit_to_celsius(f)}")