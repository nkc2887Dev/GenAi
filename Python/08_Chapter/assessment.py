### FIRST Assessment :: Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

# with open("./08_Chapter/poem.txt", "r") as a:
#     b = a.read()
#     if 'Twinkle' in b:
#         print("Exists")
#     else:
#         print("Not Exists")
# print(b)

### SECOND Assessment :: The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi- score whenever the game() function breaks the Hi-score.

# def game():
#     score = int(input("Enter Score: "))
#     a = open("./08_Chapter/hiscore.txt", "r")
#     file_score = a.read() or 0
#     if score > int(file_score):
#         b = open("./08_Chapter/hiscore.txt", "w")
#         b.write(str(score))
#         b.close()
#         print("High Scorer updated!")
#     else :
#         print("Still you are High Scorer")
#     a.close()
# game()

### THIRD Assessment :: Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

# import os

# def tables(start, end):
#     if(start > end):
#         return
#     os.makedirs("./08_Chapter/tables", exist_ok=True)
#     with open(f"./08_Chapter/tables/table{start}.txt", "w") as file:
#         for i in range(1, 11):
#             file.write(f"{start} X {i} = { start * i }\n")
#     tables(start+1, end)
        
# tables(2, 5)

### FOURTH Assessment ::  A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

# def replace(word, new):
#     with open(f"./08_Chapter/file#.txt", "r") as file:
#         text = file.read()
#         text = text.replace(word, new)
#     with open(f"./08_Chapter/file#.txt", "w") as new_file:
#         new_file.write(text)

# replace("Donkey", "#####")

### FIFTH Assessment :: Repeat program 4 for a list of such words to be censored.

# def replace(words, new):
#     with open(f"./08_Chapter/file#.txt", "r") as file:
#         text = file.read()
#     for word in words:
#         text = text.replace(word, new*len(word))
#     with open(f"./08_Chapter/file#.txt", "w") as new_file:
#         new_file.write(text)

# replace(["Donkey", "nice"], "#")

### SIXTH Assessment :: Write a program to mine a log file and find out whether it contains ‘python’.

# def find(word):
#     with open("./08_Chapter/log.txt", "r") as a:
#         b = a.read()
#     if word in b:
#         print("Exists")
#     else:
#         print("Not Exists")

# find("python")


### SEVENTH Assessment :: Write a program to find out the line number where python is present from ques 6.

# def find(word):
#     with open("./08_Chapter/log.txt", "r") as a:
#         b = a.readlines()
#         print(b)
#     total_lines = 1
#     for line in b:
#         if (word in line):
#             print(f"Yes python is present. Line no: {total_lines}")
#             break
#         total_lines += 1
#     else:
#         print("No Python is not present")

# find("python")

### EIGHT Assessment :: Write a program to make a copy of a text file dummy.txt”

# a = open("./08_Chapter/dummy.txt", "r")
# b = a.read()
# print(b)

# c = open("./08_Chapter/dummy_copy.txt", "w")
# c.write(b)
# c.close()

### NINE Assessment :: Write a program to find out whether a file is identical & matches the content of another file.

a = open("./08_Chapter/dummy.txt", "r")
b = a.read()
c = open("./08_Chapter/dummy_copy.txt", "r")
d = c.read()

if b == d :
    print("SAME")
else :
    print("NOT SAME")
a.close()
c.close()

### TENTH Assessment :: Write a program to wipe out the content of a file using python.

# with open("./08_Chapter/dummy_copy.txt", "w") as f:
#     f.write("")

### ELEVEN Assessment :: Write a python program to rename a file to “renamed_by_ python.txt.

# SAME AS EIGHT Assessment