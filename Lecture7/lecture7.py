"""recursive: 
base case
leap of faith"""

"""write an iterative and a recursive function for calculating factorial of n"""
# def rec_fact(n):
#     if (n < 2):
#         return 1
#     else:
#         return n * rec_fact(n - 1)

# def ite_fact(n):
#     i = 1
#     product = 1
#     while (i <= n):
#         product *= i
#         i += 1
#     return product

# print(rec_fact(3))
# print(ite_fact(3))

"""properties: somtimes easiest way to think about a problem
sometimes can be highly inefficient, especially in python"""

"""the structural parts of a recursive solution:
base case
recursive case
"""

"""translate design from iterative to recursive and vice versa, where applicable"""

"""Recursion helps with trees:
maximize from branches to root
iterating presents the challenge of not knowing th depth of the tree in advance
recursion works elegantly, regardless of the depth of the tree
"""
def do_something(n):
    if n > 0:
        do_something(n - 1)
        print(n, end="")
        do_something(n - 1)
"""what is the below gonna print?"""

do_something(3)
"""for loop + recursion application"""
def add_up(my_list):
    if type(my_list) == list and len(my_list) > 0:
        return add_up(my_list[0]) + add_up(my_list[1:])
    elif type(my_list) == int:
        return my_list
    else:
        return 0

def add_up_2(my_list):
    sum = 0
    for number in my_list:
        if (isinstance(number, list)):
            sum += add_up(number)
        else:
            sum += number
    return sum

l = [8, [1, 2], [2, 3, 5], 6]
print(add_up(l))
print(add_up_2(l))


"""tail recursion elimination(python does not implement this?)
Fibonacci: inefficient, repeatedly doing the same calculation, not as elegant as factorial
recursion causes stack to grow, even stack overflow"""

"""Tower of Hanoi"""
