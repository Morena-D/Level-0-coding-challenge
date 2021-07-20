import math
def calarea(a,b,c):
    s = 0.5*(a+b+c)  

    total = s*(s-a)*(s-b)*(s-c)   
    area = math.sqrt(total)

    return f"The area of the triangle is: {area}"

print(calarea(3,4,5))

