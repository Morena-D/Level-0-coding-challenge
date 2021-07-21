def calarea(a,b,c):
    s = 0.5*(a+b+c)  

    total = s*(s-a)*(s-b)*(s-c)   
    sqrt = total ** 0.5
    area = sqrt
    
    return f"The area of the triangle is: {area}"

print(calarea(3,4,5))

