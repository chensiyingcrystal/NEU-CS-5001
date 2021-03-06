while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

"""
Module: Handing Exceptions

This is the code that we are starting with in module 10.  Many changes 
will be made to the code and there will be a couple of different version
as we cover the material in this module.

Version 5 include the validation of the parameters in get_slices, 
and the handling of the errors raised in main  This one is different than
version 4 because we introduced an error
"""


def get_slices(pies, folks):
    ''' Function: get_slices that calculates the number of slices of pizza
        Params:   pies, the number of pies
                  folks, the number of people
        Returns:  the number of slices per person
    '''
    if not isinstance(folks, int):
        raise TypeError("folks must be an integer")
    if folks <= 0:
        raise ValueError("folks must be positive")
    if not isinstance(pies, int):
        raise TypeError("pies must be an integer")
    if pies < 0:
        raise ValueError("pies must be non-negative")
    slices = pies * 8 // folks
    return slices


def main():
    try:
        pizzas = int(input("How many pizzas did you order? "))
        people = int(input("How many people are there? "))
        slices = get_slices(pizzas, people)
        print(pizzas, "pizzas split", people,
              "ways is", slices, "slices each")

    except TypeError as ex:
        print("Invalid type:", type(ex), ex)
    except ValueError as ex:
        print("Invalid value:", type(ex), ex)


main()

"""collecting data, applying exceptions"""
def main():
    filename = input("Enter filename: ")
    file = open(filename, "w")

    number = int(input("Enter weight (or -1 to quit): "))
    while number != -1:
        file.write(str(number))
        number = int(input("Enter weight (or -1 to quit)"))

main()

