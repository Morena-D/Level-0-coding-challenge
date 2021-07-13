def max_number(a,b,c):
    maximum = a
    if b > a:
        maximum = b
        if c > b:
            maximum = c
    return maximum
a = 11
b = 15
c = 30
print(f"The maximum number is: {max_number(a,b,c)}")