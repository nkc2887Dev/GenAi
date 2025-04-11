## FILE I/O

# r - open for reading
# w - open for writing
# a - open for appending
# + - open for updating.
# rb - will open for read in binary mode.
# rt - will open for read in text mode.

# a = open("./08_Chapter/dummy.txt", "r")
# # b = a.read()
# b = a.readline() 
# print(b)
# a.close()

# a = open("./08_Chapter/dummy.txt", "w")
# b = a.write("this is nice")
# print(b)
# a.close()

with open("./08_Chapter/dummy.txt", "r") as c:
    text = c.read()

print(text)