## ADVANCED PYTHON 2

# LAMBDA FUNCTIONS

a = lambda x: x**2
# print(a(3))

# JOIN METHOD (STRINGS)

b = ["apple", "mango", "banana"] 
result = ",".join(b) 
# print(result)

# FORMAT METHOD (STRINGS) template.format(p1,p2...)
c = "{} is a good {}".format("Dev", "boy")  # by default sequence is 0,1,2,3,....
d = "{1} is a good {0}".format("Dev", "boy")  # we can set 

# print(c)
# print(d)

# MAP
def square(x):
    return x**2
    # return x*2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
# print(squared_numbers)

# FILTER
def is_even(x):
    return x % 2 == 0
    # return x > 2

even_numbers = list(filter(is_even, numbers))
# print(even_numbers)

# REDUCE
from functools import reduce
def add(x, y):
    return x + y

sum_of_numbers = reduce(add, numbers)
# print(sum_of_numbers)

# ZIP
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
# print(zipped)
