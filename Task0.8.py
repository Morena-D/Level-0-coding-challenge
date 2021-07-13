def time_convert(t):
    hours = t // 60   #returning only the integer part of the qoutient
    minutes = t % 60   #returning the remaing part of the qoutient
    if hours == 1 and minutes ==1:
        return f"{hours} hour and {minutes} minute"
    if hours == 1:
        return f"{hours} hour and {minutes} minutes"
    if minutes == 1:
        return f"{hours} hours and {minutes} minute"
    return f"{hours} hours and {minutes} minutes"

t = 71
print(time_convert(t))