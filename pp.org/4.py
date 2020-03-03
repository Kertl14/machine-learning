while True:
    num = input("Please enter an integer: ")
    try: 
        num = int(num)
        break
    except ValueError:
        print("That is not an integer")
        
num_list = range(1, (num + 1))

div_list = []

for i in num_list:
    if num % i == 0:
        div_list.append(i)
        
print(div_list)
