"""recursive: 
base case
leap of faith"""

"""write an iterative and a recursive function for calculating factorial of n"""
def n_rec_fact(n):
    if (n < 2):
        return 1
    else:
        return n * n_rec_fact(n - 1)

def n_ite_fact(n):
    i = 1
    product = 1
    while (i <= n):
        product *= i
        i += 1
    return product

print(n_rec_fact(3))
print(n_ite_fact(3))



