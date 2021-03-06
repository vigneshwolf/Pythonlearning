# In python we use docstring to explain how to use code. it will be useful in interactive mode and to create auto-documentation. below we see example if the docstring for a function called longest_string

import math

def longest_side(a, b):
    """
    Function to find the length of the longest side of a right triangle.

    :arg a: side a of the triangle 
    :arg b: side b of the triangle

    :return: Length of the longest side c as float
    """

    return math.sqrt(a*a + b*b)

if __name__ == '__main__':
    print(longest_side(4, 5))
