### First Assessment :: Write a program to store seven fruits in a list entered by the user.

# FIRST WAY
# a = input("Enter the first fruit: ")
# b = input("Enter the second fruit: ")
# c = input("Enter the third fruit: ")
# d = input("Enter the fourth fruit: ")
# e = input("Enter the fifth fruit: ")
# f = input("Enter the sixth fruit: ")
# g = input("Enter the seventh fruit: ")

# fruits = [a, b, c, d, e, f, g]
# print(fruits, type(fruits))

# SECOND WAY
# fruits = []
# for i in range(7):
#     fruit = input(f"Enter the {i+1} fruit: ")
#     fruits.append(fruit)
# print(fruits, type(fruits))

# THIRD WAY
# fruits = [input(f"ENter fruits {i+1}: ") for i in range(7)]
# print(fruits, type(fruits))

### Second Assessment :: Write a program to accept marks of 6 students and display them in a sorted manner.

# students = []
# for i in range(6):
#     student = input(f"enter your marks {i+1}: ")
#     students.append(student)
# students.sort(reverse=False)
# print(students, type(students))

### Third Assessment :: Check that a tuple type cannot be changed in python.

# h = (45,25)
# h[0] = 100  # TypeError: 'tuple' object does not support item assignment
# print(type(h))

### Fourth Assessment :: Write a program to sum a list with 4 numbers

# FIRST WAY
# i = [2, "4", 5, 6] # TypeError: unsupported operand type(s) for +=: 'int' and 'str'
i = [2, 4, 5, 6]
j = 0

for item in i:
    j += item
print(j, type(j))

# SECOND WAY
# numbers = []
# for i in range(4):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# total = sum(numbers)

# print("The numbers are:", numbers)
# print("The sum is:", total)

### Fifth Assessment :: Write a program to count the number of zeros in the following tuple:

k = (7, 0, 8, 0, 0, 9)
print(k.count(0))