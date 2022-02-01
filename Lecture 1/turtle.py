from turtle import *


def equitri(length):
    forward(length)
    setheading(120)
    forward(length)
    setheading(240)
    forward(length)

def square(length):
    n = 0
    while n < 4:
        forward(length)
        right(90)
        n += 1


def main():
    how_big = int(input("How big are the sides you want? "))
    equitri(how_big)
    print("Done!")
    home()
    how_big = int(input("How big are the sides you want? "))
    square(how_big)
    print("Done!")


if __name__ == '__main__':
    main()

    
