## DICTIONARY & SETS

# DICTIONARY

a = {
    "key": "value",
    "harry": "code",
    "marks": "100",
    "list": [1, 2, 9],
    "jk": "78"
}
# print(a, type(a))
# print(a["key"]) # Output: "value"
# print(a["list"]) # Output: [1, 2, 9]
# print(a.jk) # AttributeError: 'dict' object has no attribute 'jk'

# FUNCTIONS (METHODS)

b={
    "name":"dev",
    "from":"india",
    "marks":[92,98,96]
}

# print(b.items())
# print(b.keys())
# print(b.values())
# print(b.get("name"))
# b.update({"name": "NK"})
# print(b.items())

# SETS 

c = set()
print(c)
# c.add(1)
# c.add(2)
# c.update([3, 4])
# c.remove(2)    # Throws error if not found
# c.discard(10)  # No error if not found
# c.pop()        # Removes a random element
# c.clear()      # Empties the set
# print(c)

d = {1, 2, 3}
e = {3, 4, 5}

print(d)
# print(len(d))
# d.remove(2)
# d.pop()
# d.union({d,e})
# d.intersection({d,e})

print(d | e)   # Union: {1, 2, 3, 4, 5}
print(d & e)   # Intersection: {3}
print(d - e)   # Difference: {1, 2}
print(d ^ e)   # Symmetric Difference: {1, 2, 4, 5}

