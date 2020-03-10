"""General functions to gather user inputs from the console.

Usage:
    FOR IMPORT ONLY - not intended to be excecutable.
"""

def input_int(string):
    """Forces a user to provide an integer before the program can continue.
    
    Args:
        string: the prompt that you wish to supply the user.
        
    Returns:
        An integer provided by the user.
    """
    while True:
        userinp = input(string)
        try:
           userint = int(userinp)
           return userint
        except ValueError:
           print("Value must be an integer.")


def input_flo(string):
    """Forces a user to provide a number before the program can continue.
    
    Args:
        string: the prompt that you wish to supply the user.
        
    Returns:
        A float provided by the user.
    """
    while True:
        userinp = input(string)
        try:
           userflo = float(userinp)
           return userflo
        except ValueError:
           print("Value must be a number.")

           
def input_boo(string):
    """Forces a user to provide a True or False value before the program can continue.
    
    Args:
        string: the prompt that you wish to supply the user.
        
    Returns:
        A boolean provided by the user.
    """
    while True:
        userinp = input(string)
        if userinp == True or userinp == False:
           return userinp
        else:
            print("Please enter 'True or 'False'")