### FIRST Assessment :: Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

## open 12_Chapter folder in Terminal
## Run this command line by line
# python -m virtualenv env1 - create envirenment for env1
# python -m virtualenv env2 - create envirenment for env1
#  .\env1\Scripts\activate.ps1 - activate envirenment for env1
# pip install panadas - install
# pip install pyjokes - install
# pip freeze > requirements1.txt - create file of envirenmnet for env1 with version
# deactivate - deactivate envirenment for env1
# .\env2\Scripts\activate.ps1
# pip install -r .\requirements1.txt - can recreate the same environment 
# pip freeze > requirements2.txt - create file of envirenmnet for env2 with version
# deactivate - envirenment for env2


### SECOND Assessment :: Write a program to input name, marks and phone number of a student and format it using the format function like below: “The name of the student is Dev, his marks are 72 and phone number is 99999888”

# name = input("Enter name: ")
# marks = int(input("Enter marks: "))
# phone = input("Enter phone number: ")
# print("The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone))

### THIRD Assessment :: A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
# table = [str(7*i) for i in range(1, 11)]
# a = "\n".join(table)
# print(a)

### FOURTH Assessment ::  Write a program to filter a list of numbers which are divisible by 5.

# def filer_out(n):
#     if n%5 == 0:
#         return True
#     else:
#         return False
# b = list(filter(filer_out, [1,2,5,7,50,56,25]))
# print(b)


### FIFTH Assessment :: Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

def max_num(a, b):
    if a > b:
        return a
    else:
        return b
c = reduce(max_num, [1, 2, 5, 7, 50, 56, 25])
print(c)

### SIXTH Assessment :: Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

# pip freeze > requirements.txt
# python -m virtualenv env6
# .\env6\Scripts\activate.ps1
# pip install -r .\requirements.tx
# pip freeze > requirements6.txt
# deactivate

### SEVENTH Assessment :: Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Dev!</p>"

app.run()