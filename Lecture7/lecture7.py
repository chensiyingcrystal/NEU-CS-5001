"""recursive: 
base case
leap of faith"""

"""write an iterative and a recursive function for calculating factorial of n"""
def rec_fact(n):
    if (n < 2):
        return 1
    else:
        return n * rec_fact(n - 1)

def ite_fact(n):
    i = 1
    product = 1
    while (i <= n):
        product *= i
        i += 1
    return product

print(rec_fact(3))
print(ite_fact(3))

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

