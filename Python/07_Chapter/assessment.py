### FIRST Assessment :: Write a program using functions to find greatest of three numbers.

# def greatestnum(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else : 
#         return c

# a = int(input("Enter 1: "))
# b = int(input("Enter 1: "))
# c = int(input("Enter 1: "))

# d = greatestnum(a,b,c)
# print(f"greatest Number: {d}")

### SECOND Assessment :: Write a python program using function to convert Celsius to Fahrenheit.

# def convert(cel):
#     f = cel * (9/5) + 32
#     return f
# print(convert(0))
    

### THIRD Assessment :: How do you prevent a python print() function to print a new line at the end.

# print("a")
# print("b")
# print("c", end="")
# print("d", end="")
# print("e")

### FOURTH Assessment ::  Write a recursive function to calculate the sum of first n natural numbers.

# def fr(n):
#     sum = 0
#     i = 1
#     while(i<=n):
#         sum += i
#         i = i +1
#     return sum
# print(fr(4))

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print(sum(4))

### FIFTH Assessment :: Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# def pattern(n):
#     if(n==5):
#         return
#     print("*" * n)
#     pattern(n+1)
    
# pattern(1)
# pattern(3)

### SIXTH Assessment :: Write a python function which converts inches to cms.

# 1 inch is equal to 2.54 centimeters

# def convert(inch):
#     cms = inch * 2.54
#     return cms
# print(convert(10))


### SEVENTH Assessment :: Write a python function to remove a given word from a list ad strip it at the same time.

# def rem(l, word):
#     n = [] 
#     for item in l:
#         if not(item == word):
#             # n.append(item) # add full word like NKan ==> NKan
#             n.append(item.strip(word)) # remove word from existing item like NKan ==> NK
#     return n


# l = ["Dev", "NKan", "Sachin", "an"]

# print(rem(l, "an"))


### EIGHT Assessment :: Write a python function to print multiplication table of a given number.

def multi(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

multi(5)