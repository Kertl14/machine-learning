def __idsuffix__(x):
    s = str(x)
    if s.endswith("11"):
        return "th"
    elif s.endswith("12"):
        return "th"
    elif s.endswith("13"):
        return "th"
    elif s.endswith("1"):
        return "st"
    elif s.endswith("2"):
        return "nd"
    elif s.endswith("3"):
        return "rd"
    else:
        return "th"

def __numformat__(x):
    numstr = str(x)
    final = numstr + __idsuffix__(x)
    return final
    
while True:
    num = input("Please enter an Integer or type 'stop' to exit: ")
    if num == "stop":
        break
    try:
        num = int(num)
        print(__numformat__(num))
    except ValueError:
        print("That is not an Integer.")
    
