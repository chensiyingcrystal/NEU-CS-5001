#Over view
"""Explain what a value is and how to write statements that assign values"""
# name and value; type is decided by the value;
# '=' means 'gets the value'; '==' means 'is equivalent to'; 
# 'is' means 'the same memory loacation', point to the same object;
"""Distinguish between basic types, including integers, floats, and strings"""
# ints can be arbitrarily large
# floats are stored in ISO/IEC format from C language
"""Manipulate vars using arithmetic operators to perform calculations"""
#precision
#string concatenation
#use \ for escape character
"""Describe and use std conventions for naming variables and writing code"""

"""Define a Boolean expresstion and understand its use"""
# question:  is, python's location
# compare: use unicode for character comparing
def main():
    pizzas = int(input("how many pizzas"))
    people = int(input("how many people"))
    try:
        slices_average = pizzas * 8 / people
    except ZeroDivisionError:
        print("people cannot be 0")

"""Common Errors"""
# Syntax Error
# Logic Error: Tautology; Contradiction; 
# Confusion, inefficient booleans( use several logic laws to improve)
# Inefficient algorithms
# Short circuit evaluation


"""Patterns in Programming"""
# Decompose problem into simpler subproblems
# split the hypothesis space (eg binary search)
# Modify existing solution to analogous or related problem 
# Debug an almost-right approach: isolate each; common bug names; temporary print statement; debugging tools(tracing(in recursion), single-stepping)