"""Reformats and prints a number as a string with the correct 'nth' suffix.

Usage:
    python3 suffix.py <number>
"""

import sys

def idsuffix(x):
    """Identifies the correct suffix to use for the number argument.
    
    Args:
        x: number that the suffix should be retrieved for.
        
    Returns:
        Just the appropriate suffix.
    """
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


def numformat(x):
    """Returns a string that contains the concatenated value of the number argument and its appropriate suffix.
       
    Args:
        x: the number to be returned.
        
    Returns:
        The number plus its apprpriate suffix.
    """
    numstr = str(x)
    final = numstr + idsuffix(x)
    return final
    
    
def main(num):
    print(numformat(num))
    
    
if __name__ == "__main__":
    main(sys.argv[1])