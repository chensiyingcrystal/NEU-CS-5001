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

# modify/add the key's value // dict[key] = value // adding by assigning
# delete an element // del dict[key]

# iterate over a dictionary
# for key in dict:
# items method returns an object that can be iterated over like a for loop
# dict.items()
# for key_val_pair in dict.items():
    # print key_val_pair
# or// for key, value in dict.items():


"""Set in python
unordered collection of distinct members # a set of keys
# items must be immutable
# order does not matter
# items must be unique"""

"""To make an empty set
my_set = {}  # this is an empty dictionary
my_set = set()  # this is an empty set"""

# initialize: my_set = {1, 2, 3}
# add elements: my_set.add('xyz')
# delete elements: my_set.remove('xyz')

"""Using sets in python
union |
intersection &
difference -
subset <="""

"""Using JSON in python"""

"""Programs = Algorithms + Data Structures
Set can be useful in math and logical case
Dictionaries workd especially well with JSON "light database" files
stack frames can be thought of as a dictionary of identifier bindings"""
"""Highlighting these in final project is encouraged"""

import json
 
# # list conversion to Array
# print(json.dumps(['Welcome', "to", "GeeksforGeeks"]))
 
# # tuple conversion to Array
# print(json.dumps(("Welcome", "to", "GeeksforGeeks")))
 
# # string conversion to String
# print(json.dumps("Hi"))
 
# # int conversion to Number
# print(json.dumps(123))
 
# # float conversion to Number
# print(json.dumps(23.572))
 
# # Boolean conversion to their respective values
# print(json.dumps(True))
# print(json.dumps(False))
 
# # None value to null
# print(json.dumps(None))

# var = {
#       "Subjects": {
#                   "Maths":85,
#                   "Physics":90
#                    }
#       }

# with open("sample.json", "w") as p:
#     json.dump(var, p)

# with open("Sample.json", "r") as read_it:
#      data = json.load(read_it)
    
# print(data)
# print(type(data))

json_var ="""
{
    "Country": {
        "name": "INDIA",
        "Languages_spoken": [
            {
                "names": ["Hindi", "English", "Bengali", "Telugu"]
            }
        ]
    }
}
"""
var = json.loads(json_var)
print(var)
print(type(var))