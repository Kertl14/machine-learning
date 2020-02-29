thisYear = 2020

name = input("What is your name?: ")

age = 0

while True:
    age = input("How old are you?: ")
    try: 
        age = int(age)
        break
    except ValueError:
        print("Please enter an Integer.")
        
while True:
    num = input("How many times should the response be printed?: ")
    try: 
        num = int(num)
    except ValueError:
        print("Please enter a positive Integer.")
    if num <= 0:
        print("Please enter a positive Integer.")
    else:
        break
    
year100 = (thisYear - age) + 100

counter = 0

while counter != num:
    print("Thanks " + name + ", you will turn 100 in the year " + str(year100))
    counter += 1
    
    