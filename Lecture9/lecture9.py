"""Aggregations of individual data elements
strings; lists; tuplesl
Other data structure: for expressive convenience; better performance
Dictionary: unique key
Set: math sets concept to organize data"""

# Dictionary:
# Key must be immutable, unique
# Key value pair
# {} delimit; 

# Three different ways to initialize a dictionary:
# dic = {'A':3, 'B':4} // most typical key-value pair
# dic([('A',3), ('B', 4)])  // group key and value in a tuple format;convert tuples into dic
# dic(A=3, B=4)  //similar to assigning variables to values; no need to quote

# 'A' in dic // to check if the key is in the dictionary
# This will return True

# modify/add the key's value // dict[key] = value
# delete an element // del dict[key]

# iterate over a dictionary
# for key in dict:
# items method returns an object that can be iterated over like a for loop
# dict.items()
# for key_val_pair in dict.items():
    # print key_val_pair