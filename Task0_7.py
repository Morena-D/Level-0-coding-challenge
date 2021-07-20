def celsius_to_fahrenheit(c):
    fahrenheit = (c * (9/5)) + 32   
    return fahrenheit

def fahrenheit_to_celsius(f):
    celsius = (f - 32) * (5/9)   
    return celsius

print(f"The temperature from celsius to Fahrenheit is {celsius_to_fahrenheit(80)}")
print(f"The temperature from Fahrenheit to Celsius is {fahrenheit_to_celsius(80)}")
