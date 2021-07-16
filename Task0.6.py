def maximum(a,b,c):
    maxi = a
    if b > a and c < b:
        maxi = b
    elif c > b and a < c:
        maxi = c
    return maxi
print(f"The maximum number is: {maximum(4,2,7)}")
