### FIRST Assessment :: Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        print(f"hello {self.name}, Age: {self.age}, Salary: {self.salary}")

# a = Programmer("A", 20, 2000)
# b = Programmer("B", 22, 6000)

### SECOND Assessment :: Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, num):
        self.num = num
        # print(f"Square: {self.num**2}, Cube: {self.num**3}, Square Root: {self.num**0.5}")
    
    def cal(self): 
        print("Enter a number: ")
        num = int(input())
        # a = Calculator(num)
        print(f"Square: {self.num**2}, Cube: {self.num**3}, Square Root: {self.num**0.5}")

# c = Calculator(2)
# c.cal()

### THIRD Assessment :: Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class A:
    a = 10
    pass

# d = A()
# print(d.a)
# d.a = 0
# print(d.a)

### FOURTH Assessment ::  Add a static method in problem 2, to greet the user with hello.

class Calculator:

    def __init__(self, name):
        self.name = name
        print(f"Hello Class {self.name}")

    @staticmethod
    def greet(nm):
        print(f"Hello {nm}")

# e = Calculator("dev")
# e.greet("NK")


### FIFTH Assessment :: Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_fare_info(self):
        print(f"The fare of {self.name} is: {self.fare}")

    def get_status(self):
        print(f"the available seats for {self.name} is {self.seats}")

    def book_ticket(self):
        if(self.seats > 0):
            print(f"booked ticket in {self.name}")
            self.seats = self.seats -1
        else:
            print("Sorry, no seats available")

# f = Train("Rajdhani", 90, 3)
# f.get_fare_info()
# f.book_ticket()
# f.get_status()


### SIXTH Assessment :: Can you change the self-parameter inside a class to something else (say dev). Try changing self to “slf” or dev and see the effects.

class Change:
    def __init__(slf, name):
        slf.name = name

    def change_name(dev, nm):
        print(f"Hello, {dev.name}")
        print(f"Hello, {nm}")

# g = Change("NK")
# g.change_name("dev23")
