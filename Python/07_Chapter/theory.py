## FUNCTIONS & RECURSIONS

def first(name):
    print(f"Good day {name}")

name = input("Enter Name: ")

first(name)

def second (name = "stranger"):
    greet = "Hello " + name
    return greet


res = second("Dev")
res2 = second()
print(res)
print(res2)


# RECURSION

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else :
        return x * factorial(x-1)

res3 = factorial(3)
print(res3)