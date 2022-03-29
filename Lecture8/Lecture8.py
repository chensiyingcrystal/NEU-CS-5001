"""Error handling"""
"""AttributeError()
ValueError() vs TypeError()
ZeroDivisionError()
NameError()
IndexError()
ImportError()"""

"""Include a suite of test cases:
make sure that all existing tests must continue to pass"""

"""consider unpredictability of end useres:
end-user keyboard input"""

"""produce informative error messages"""

"""try/except"""

"""handling I/O error"""
FileNotFoundError()
PermissionError()
OSError()

try:
    with open('too.txt', 'r') as f:
        #process content
    except IOError as ex:
        print("An Unexpected IOError occurred opening ")




