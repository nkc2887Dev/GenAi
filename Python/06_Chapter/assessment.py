### FIRST Assessment :: Write a program to print multiplication table of a given number using for loop.

# a = int(input("Enter number: "))
# for i in range(1, 11):
#     b = i * a
#     print(f"{a} X {i} = {b}")

### SECOND Assessment :: Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

# c = ["Dev", "NK", "Sachin", "Rahul"]

# for i in c:
#     if(i.startswith("S")):
#         print(f"Hello {i}")


### THIRD Assessment :: Attempt problem 1 using while loop.

# d = int(input("Enter number: "))
# i = 1
# while(i <= 10):
#     print(f"{d} X {i} = {d*i}")
#     i = i+1

### FOURTH Assessment ::Write a program to find whether a given number is prime or not.

# e = int(input("Enter a number: "))

# for i in range(2, e):
#     if(e%i) == 0:
#         print("not prime")
#         break
# else:
#     print("Prime")

### FIFTH Assessment :: Write a program to find the sum of first n natural numbers using while loop.

# f = int(input("Enter a number: "))
# i =1
# e = 0
# while (i<=f):
#     e += i
#     i = i+1
# print(e)

### SIXTH Assessment :: Write a program to calculate the factorial of a given number using for loop.

# g = int(input("Enter a number: "))
# i=1
# h =1
# while(i<=g):
#     h = h * i
#     i = i+1
# print(h)

### SEVENTH Assessment :: Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3
l = int(input("Enter the number: "))
for i in range(1, l+1):
    print(" "* (l-i), end="")
    print("*"* (2*i-1), end="")
    print("")

### EIGHT Assessment :: Write a program to print the following star pattern.
# *
# **
# *** for n = 3
m = int(input("Enter the number: "))
for i in range(1, m+1): 
    print("*"* i, end="")
    print("")

### NINE Assessment :: Write a program to print the following star pattern.
# ***
# * * for n = 3
# ***
n = int(input("Enter the number: "))
for i in range(1, n+1): 
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")

### TENTH Assessment :: Write a program to print multiplication table of n using for loops in reversed order.

# j = int(input("Enter number: "))
# for i in range(-10, 0):
#     k = i * j
#     print(f"{j} X {i} = {k}")

# for i in range(1, 11):
#     print(f"{j} X {11 -i} = {j*(11-i)}")