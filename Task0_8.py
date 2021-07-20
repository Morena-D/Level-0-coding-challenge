def time_convert(t):
    hours = t // 60   
    minutes = t % 60   
    if hours == 1 and minutes ==1:
        return f"{hours} hour and {minutes} minute"
    if hours == 1:
        return f"{hours} hour and {minutes} minutes"
    if minutes == 1:
        return f"{hours} hours and {minutes} minute"
    return f"{hours} hours and {minutes} minutes"

print(time_convert(71))
