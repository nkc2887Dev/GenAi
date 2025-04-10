## LISTS AND TUPLES

a = ["dev", 45, 3.14, True, None, "hello"]
# print(a, type(a))
# print(a, type(a[0]))
# print(a, type(a[1]))
# print(a, type(a[2]))
# print(a, type(a[3]))
# print(a, type(a[4]))
# print(a, type(a[5]))
# print(a, type(a[6]))  # IndexError: list index out of range
# print(a[0:3])  # [start index:end index]
# print(a[:3])  # same as [0:3]
# print(a[1:])  # same as [1:end index]
# print(a[1:3])  # [start index:end index]
# print(a[1:3:2])  # [start index:end index:step size]
# print(a[1::2])  # [start index::step size]
# print(a[::2])  # [::step size]

# FUNCTIONS (METHODS)
# print(a)
# print(len(a))
# print(a.count("dev"))
# print(a.index("dev"))
# a.append("hello2")
# a.insert(1, "hello")
# a.extend(["hello", "world"])
# a.remove("hello")
# a.pop()
# a.pop(1)
# a.clear()
# a.copy()
# print(a)

b = [34,5,6,7,8,45, 78, 20, 9, 2, 4,5]
# print(b)
# b.sort()
# b.reverse()
# b.sort(reverse=True)
# b.sort(reverse=False)
# print(b)


## TUPLES
c = ("dev", 45, 3.14, True, None, "hello") # tuple with more than one element
d = () # empty tuple
e = (67,) # tuple with only one element needs a comma

# print(c, type(c))
# print(d, type(d))
# print(e, type(e))
# print(c, type(c[0]))
# print(c, type(c[1]))
# print(c, type(c[2]))
# print(c, type(c[3]))
# print(c, type(c[4]))
# print(c, type(c[5]))
# print(c, type(c[6]))  # IndexError: tuple index out of rcnge
# print(c[0:3])  # [start index:end index]
# print(c[:3])  # same cs [0:3]
# print(c[1:])  # same cs [1:end index]
# print(c[1:3])  # [start index:end index]
# print(c[1:3:2])  # [start index:end index:step size]
# print(c[1::2])  # [start index::step size]
# print(c[::2])  # [::step size]
# print(c.count("dev"))
# print(c.index("dev"))
print(c.index("dev", 0, 3))
print(c.index(5))  # ValueError: tuple.index(x): x not in tuple