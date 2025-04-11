## OBJECT ORIENTED PROGRAMMING

class Employer:
    def __init__(self, name):
        self.name=name
    def get_name(self):
        print("Hello", self)

    @staticmethod
    def greet(name):
        print(f"name: {name}")
        return f"name: {name}"

a = Employer("DEV")
b = a.greet("def")
print(b)