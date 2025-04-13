### FIRST Assessment :: Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class TwoD:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"2D vector: (x: {self.x}, y: {self.y})")

class ThreeD(TwoD):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        print(f"3D vector: (x: {self.x}, y: {self.y}, z:{self.z})")

# a = TwoD(1, 2)
# b = ThreeD(1, 2, 3)

### SECOND Assessment :: Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def __init__(self, name):
        print(f"Animal: {self.name}")

class Pets(Animals):
    def __init__(self, name):
        super().__init__(name)
        print(f"Pets: {self.name}")

class Dog(Pets):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        print(f"Dog: {self.name}")
    
    def bark(self):
        print(f"\"{self.name}\" is barking - Bow Bow!")

# c = Dog("Tommy")
# c.bark()

### THIRD Assessment :: Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    def __init__(self, salary):
        self.salary = salary
        print(f"Your current salary is {self.salary}.")

    @property
    def salaryAfterIncrement(self):
        return f"After increment the salary will be {self.sai}%"

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self.sai = self.salary + (self.salary * value / 100)

# d = Employee(10000)
# d.salaryAfterIncrement = 1.5
# print(d.salaryAfterIncrement)
# print(d.sai)

### FOURTH Assessment ::  Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, num):
        self.num = num
        print(f"Complex number: {self.num}")

    def __add__(self, num2):
        return self.num + num2.num

    def __mul__(self, num2):
        return self.num * num2.num

# e = Complex(4)
# f = Complex(3)
# print(e+f)
# print(e*f)

### FIFTH Assessment :: Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, vec):
        self.vec = vec
        print(f"Vector: {self.vec}")

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        dot = 0
        for i in range(len(self.vec)):
            dot += (self.vec[i] * vec2.vec[i])
        return dot

# g = Vector([1, 2, 3])
# h = Vector([3, 2, 5])
# print(g+h)
# print(g*h)

### SIXTH Assessment :: Write __str__() method to print the vector as follows:

class String:
    def __init__(self, vec):
        self.vec = vec
        print(f"Vector: {self.vec}")

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

# i = String([7, 8, 10])
# print(str(i))

### SEVENTH Assessment :: 


class Length:
    def __init__(self, vec):
        self.vec = vec
        print(f"Vector: {self.vec}")

    def __len__(self):
        return len(self.vec)

# j = Length([1,2,1,8])
# print(len(j))