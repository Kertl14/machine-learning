while True:
    num = input("Please enter a maximum value: ")
    try: 
        num = float(num)
        break
    except ValueError:
        print("Please enter a number")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

x = [i for i in a if i < num]

print(x)
        