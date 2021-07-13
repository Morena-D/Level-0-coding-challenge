def max_number(a,b,c,d,e):
    maximum = a
    if b > a:
        maximum = b
    if c > b:
        maximum = c
    if d > c:
        maximum = d
    if e > d:
        maximum = e
    return maximum
a = 300
b = 203
c = 101
d = 90
e = 88
print(f"The maximum number is: {max_number(a,b,c,d,e)}")