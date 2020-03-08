while True:
    print("please enter a positive integer, or type 'stop to exit")
    num = input()
    if num == "stop":
        break
    else: 
        try:
            num = int(num)
            if num <= 0:
                print("That is not a positive integer.")
            else:
                counter = 0
                print("Counting....")
                while counter != (num + 1):
                    print(counter)
                    counter += 1
        except ValueError:
            print("That is not a valid integer")
