'''Create a Python module that contains functions for common mathematical operations (e.g., factorial, greatest common divisor). Write a script
that imports this module and uses its functions.'''

import math

def factorial(n):
   
    return math.factorial(n)

def gcd(a, b):
    
    while b:
        a, b = b, a % b
    return a
