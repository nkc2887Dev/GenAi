### First Assessment :: Write a python program to display a user entered name followed by Good Afternoon using input () function

# a = input("Enter a name: ")
# print(f"Good Afternoon {a}!")

### Second Assessment :: Write a program to fill in a letter template given below with name and date.
from datetime import date

b = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(b.replace("<|Name|>", "Dev").replace("<|Date|>", str(date.today())))

### Third Assessment :: Write a program to detect double space in a string.

c = "This is a string with double  space"
print(c.find("  "))

### Fourth Assessment :: Replace the double space from problem 3 with single spaces.

print(c.replace("  ", " "))

### Fifth Assessment :: Write a program to format the following letter using escape sequence characters.

d = "Dear Dev, \n\tthis \"python\" course is nice. \nThanks!"
print(d)