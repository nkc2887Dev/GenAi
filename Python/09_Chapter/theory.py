## OBJECT ORIENTED PROGRAMMING

class Employer:
    def __init__(self, name): # constructor || __init__() is a special method which is first run as soon as the object is created.
        self.name=name
        
    def get_name(self):
        print("Hello", self)

    @staticmethod
    def greet(name):
        print(f"name: {name}")
        return f"name: {name}"

a = Employer("DEV")
b = a.greet("def")
# c = a.get_name() #equivalent to Employer.get_name(a)

print(b)