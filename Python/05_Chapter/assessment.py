### FIRST Assessment :: Write a program to find the greatest of four numbers entered by the user.

# FIRST WAY
# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1:", a1)

# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number is a2:", a2)

# elif(a3>a1 and a3>a2 and a3>a4):
#     print("Greatest number is a3:", a3)

# elif(a4>a1 and a4>a2 and a4>a3):
#     print("Greatest number is a4:", a4)

# SECOND WAY
# a = 0;
# for i in range(4):
#     b = int(input("ENter your number: "))
#     if (b > a):
#         a = b

# print(a)

### SECOND Assessment :: Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# b1 = int(input("Enter Aptitude Marks: "))
# b2 = int(input("Enter Reasoning Marks: "))
# b3 = int(input("Enter English Marks: "))
# sum = b1 + b2 + b3

# if(100*(sum/300) >= 40 and b1 >= 33 and b2 >= 33 and b3 >= 33):
#     print("You Passed in Exam.")
# else :
#     print("You Failed in Exam.")

### THIRD Assessment :: A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# c1 = "Make a lot of money"
# c2 = "buy now"
# c3 = "subscribe this"
# c4 = "click this"

# c5 = input("Enter you comments: ")

# if((c1 in c5) or (c2 in c5) or (c3 in c5) or (c4 in c5)):
#     print("there is spam comment detect")
# else :
#     print("there is no spam comment")

### FOURTH Assessment :: Write a program to find whether a given username contains less than 10 characters or not.

# d = input("Enter your name: ")

# if(len(d) < 10):
#     print("yes Less than")
# else :
#     print("No")

### FIFTH Assessment :: Write a program which finds out whether a given name is present in a list or not.

# e = ["dev", "nk", "python"]

# f = input("Enter your name: ")

# if(f in e):
#     print("Yes")
# else :
#     print("NO")

### SIXTH Assessment :: Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# g = int(input("Enter your marks: "))

# if (90 < g and g < 100) :
#     print("Ex")
# elif (80 < g and g < 90):
#     print("A")
# elif (70 < g and g < 80):
#     print("B")
# elif (60 < g and g < 70):
#     print("C")
# elif (50 < g and g < 60):
#     print("D")
# else :
#     print("failed")


### SEVENTH Assessment :: Write a program to find out whether a given post is talking about Dev or not.

# h = input("Enter your post: ")

# if("dev" in h.lower()):
#     print("Yes")
# else :
#     print("NO")