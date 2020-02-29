while True:
    che = input("Please enter a number to check: ")
    try: 
        che = float(che)
        break
    except ValueError:
        print("That is not a number")
        
while True:
    div = input("Please enter a number to divide by: ")
    try: 
        div = float(div)
        break
    except ValueError:
        print("That is not a number")
        
if che % div == 0:
    print("These numbers are evenly divisible")
else:
    print("These numbers are not evenly divisible")