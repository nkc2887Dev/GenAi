### FIRST Assessment :: Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

# try:
#     with (
#         open("sample.txt", "r") as f,
#         open("sample2.txt", "r") as f2,
#         open("sample3.txt", "r") as f3,
#     ):
#         data = f.read()
#         data2 = f2.read()
#         data3 = f3.read()

# except FileNotFoundError as e:
#     print("File not found: ", e)

### SECOND Assessment :: Write a program to print third, fifth and seventh element from a list using enumerate function.

# list = [1,2,3,4,5,6,7,8,9,0]
# for index, item in enumerate(list):
#     if index == 2 or index == 4 or index == 6:
#         print(f"The {index+1}th element is {item}")

### THIRD Assessment :: Write a list comprehension to print a list which contains the multiplication table of a user entered number.

def table(n):
    a = [f"{n} x {i} = {n*i}" for i in range(1, 11)]
    print(a)

# n = int(input("Enter the number: "))
# table(n)

### FOURTH Assessment ::  Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.
# try:
#     a = int(input("Enter the first Number: "))
#     b = int(input("Enter the second Number: "))

#     if(b == 0):
#         raise ZeroDivisionError("Zero Division Error by raise")
#     else:
#         print(a/b)
# except Exception as e:
#     print(e)



### FIFTH Assessment :: 

def table(n):
    a = [f"{n} x {i} = {n*i}" for i in range(1, 11)]
    print(a)
    with open("11_Chapter/table.txt", "a") as f:
        f.write(str(a) + "\n")

n = int(input("Enter the number: "))
table(n)
