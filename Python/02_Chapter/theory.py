## STRINGS

a = 'single quote'
b = "double quote"
c = '''triple single quote'''
d = """triple double quote"""

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))

name = "Dev Chudasama"
# SLICING
# print(name[0]) # positive slicing
# print(name[-1]) # negative slicing
# print(name[1:6])
# print(name[:6]) # same as [start index:6]
# print(name[1:]) # same as [1:end index]
# print(name[1:6:3]) # [start index:end index:step size]
# print(name[1::2]) # [start index::step size]

# FUNCTIONS (METHODS)
print(len(name))
print(name.startswith("Dev"))
print(name.endswith("sh"))
print(name.count("a"))
print(name.capitalize())
print(name.find("a"))
print(name.lower())
print(name.islower())
print(name.upper())
print(name.isupper())
print(name.replace("a", "A"))
print(name.title())
print(name.istitle())
print(name.swapcase())
print(name.isalnum())
print(name.isalpha())
print(name.isnumeric())
print(name.isprintable())
print(name.isspace())
print(name.split())
print(name.splitlines())
print(name.partition("a"))
print(name.rpartition("a"))
print(name.rsplit())
print(name.rstrip())
print(name.lstrip())

# ESCAPE SEQUENCE CHARACTERS
esc = "hello sir\n\tMy \"name\" is Dev\nThank You"
print(esc) 