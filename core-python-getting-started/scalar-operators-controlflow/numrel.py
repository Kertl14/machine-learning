while True:
    print("Please enter an integer, or type 'stop' to exit.")
    num = input()
    if num == "stop":
        break
    else: 
        try:
            num = int(num)
            if num > 0 and num <= 5:
                print("num is greater than zero!")
            elif num > 5:
                print("num is greater than 5!")
            elif num < 0 and num >= -5:
                print("num is less than zero!")
            elif num < -5:
                print("num is less than -5!")
            elif num == 0:
                print("The number is Zero!")
        except ValueError:
            print("You did not enter a valid integer.")

    
