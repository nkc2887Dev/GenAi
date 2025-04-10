### First Assessment :: Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

# FIRST WAY
# words = {
#     "madad": "Help",
#     "kursi": "Chair",
#     "billi": "Cat"
# }

# word = input("Enter the word you want meaning of: ")

# print(words[word])

# SECOND WAY
a = {
    "water": "पानी",
    "salt": "नमक",
    "book": "किताब",
    "apple": "सेब",
    "dog": "कुत्ता",
    "cat": "बिल्ली",
    "house": "घर",
    "road": "सड़क",
    "school": "स्कूल",
    "friend": "मित्र"
}

# while True:
#     b = input("Enter the word you want meaning of: ")

#     if b == 'exit':
#         print("Exiting dictionary. Goodbye!")
#         break

#     translation = a.get(b)

#     if translation:
#         print(f"➡️ Hindi translation: {translation}\n")
#     else:
#         print("❌ Word not found in the dictionary.\n")

### Second Assessment :: Write a program to input eight numbers from the user and display all the unique numbers (once).

# c = set()

# for i in range(8):
#     d = int(input("Enter values : "))
#     c.add(d)

# print(c)

### Fourth Assessment :: Can we have a set with 18 (int) and '18' (str) as a value in it?

# e = set()
# e.add(18)
# e.add("18")
# print(e)

### Fifth Assessment :: What will be the length of following set f:

# f = set()
# f.add(20)
# f.add(20.0)
# f.add('20')
# print(len(f))

### SIXTH Assessment :: What is the type of 'g'?

# g = {}
# print(g, type(g))

### SIXTH Assessment :: Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

# h = {}
# for i in range(4):
#     key = input("Enter your name: ")
#     value = input("Enter your fav language: ")
#     # h.update({ key: value })
#     h[key] = value
# print(h)



### SEVENTH Assessment :: If the names of 2 friends are same; what will happen to the program in problem 6?

# If two friends enter the same name, the dictionary will overwrite the previous entry because dictionary keys must be unique.

### EIGHT Assessment :: If languages of two friends are same; what will happen to the program in problem 6?

# In a dictionary, values can be duplicated, only keys must be unique.

### NINE Assessment :: Can you change the values inside a list which is contained in set j?)

# j = { 8, 7, 12, "Dev", [1,2] }  # ❌ TypeError: unhashable type: 'list'
j = {8, 7, 12, "Dev", (1, 2)}  # ✅ This is valid
j[4][0] = 9 # TypeError: 'set' object is not subscriptable
print(j)

# 1 List of Lists – if you want to be able to modify inner values
k = [8, 7, 12, "Harry", [1, 2]]  # ✅ Valid

# You can now modify the list inside
k[-1][0] = 99
print(k)  # Output: [8, 7, 12, 'Harry', [99, 2]]

# 2. Set of Tuples – if you want set behavior (no duplicates) and fixed data
l = {8, 7, 12, "Harry", (1, 2)}  # ✅ Valid set

# You cannot change the (1, 2) tuple itself — but you can remove and add
l.remove((1, 2))
l.add((99, 2))
print(l)  # Output: {99, 2, 7, 8, 12, 'Harry'} depending on order
