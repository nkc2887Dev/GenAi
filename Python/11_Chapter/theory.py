## ADVANCED PYTHON 1

# WALRUS OPERATOR (:=)

# if(n := len([2,5,6]) == 2):
#     print("The length of the list is 2")
# else:
#     print("The length of the list is not 2")

# TYPES DEFINITIONS

# a : int = 45
# print(a)

def greet(name:str) -> str:
    print("Hello, " + name + "!")

# greet("dev")

# ADVANCED TYPE HINTS

from typing import List, Tuple, Dict, Union 

# List of integers 
numbers: List[int] = [1, 2, 3] 

# Tuple of a string and an integer 
person: Tuple[str, int] = ("Dev", 30) 

# Dictionary with string keys and integer values 
scores: Dict[str, int] = {"Dev": 90, "NK": 85} 

# Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123" 
identifier = 123 # Also valid


# MATCH CASE

def checkStatus(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
# a = checkStatus(200)
# print(a)

# DICTIONARY MERGE & UPDATE OPERATORS

b = {"a":1, "b":2}
c = {"b":1, "c":2}
# print({**b, **c})
# print(b | c)
# # print(b |= c)
# b.update(c)
# print(b)

# MULTIPLE FILE OPEN

# with ( 
#     open('file1.txt') as f1, 
#     open('file2.txt') as f2 
# ): 
# Process files

# EXCEPTION HANDLING IN PYTHON

# try:
#     a = int(input("Enter a number: " ))
#     print(a)
#     if(a == 0):
#         raise ZeroDivisionError("Zero Division Error")

# except ZeroDivisionError as e:
#     print("Zero Division Error: ", e)

# except TypeError as e:
#     print("Type Error: ", e)

# except Exception as e:
#     print("General Error: ", e)

# else:
#     print("No Error")
# finally:
#     print("Finally block")

def check_finaly():
    try:
        print(1)
        return 1
    except Exception as e:
        print(e)
        return e
    print("hhjh")
    # finally:
    #     print(2)
    #     return 2
# check_finaly()

# IF __NAME__== ‘__MAIN__’ IN PYTHON
# from module import myFunc

# THE GLOBAL KEYWORD
def fun(): 
    global a
    a = 3
    print(a)


# fun()
# print(a)

# ENUMERATE FUNCTION

# list1 = [1,7,12,11,22]
# for index, item in enumerate(list1): 
#     print(f" index {index} of {item}")

# LIST COMPREHENSIONS

# list2 = [item**2 for item in list1 if item > 8]
# print(list2)