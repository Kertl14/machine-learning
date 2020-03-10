"""Shows the relationship between a consol input and the numbers 5, 0, and -5.

Usage:
    python3 numrel.py
"""


from inputs import input_int


def numrel():
    num = input_int("Please enter an Integer: ")
    if num > 0 and num <= 5:
        print("num is greater than zero!")
    elif num > 5:
        print("num is greater than 5!")
    elif num < 0 and num >= -5:
        print("num is less than zero!")
    elif num < -5:
        print("num is less than -5!")
    elif num == 0:
        print("The number is zero!")

            
if __name__ == '__main__':
    numrel()







    
