## INHERITANCE & MORE ON OOPS

# SINGLE INHERITANCE
# class Employer:
#     company = "MicroSoft"
#     def __init__(self, name):
#         self.name = name
#         print(f"constructor of E {self.company}")
    
#     def show(self):
#         print(f"hello {self.name}")

# # a = Employer("dev")
# # a.show()

# class Coder(Employer):
#     lan = "Python"
#     def __init__(self, name):
#         self.name = name
#         print(f"constructor of C {self.lan}")
    
#     # def show(self):
#     #     print(f"hello {self.name}")
    
# # b = Coder("Dev")
# # b.show()

# MULTIPLE INHERITANCE

# class Employer:
#     company = "MicroSoft"
#     def __init__(self, name):
#         self.name = name
#         print(f"constructor of E {self.company}")
    
#     def show(self):
#         print(f"hello {self.name}")

# class Coder():
#     lan = "Python"
#     def __init__(self, name):
#         self.name = name
#         print(f"constructor of C {self.lan}")

#     def showLan(self):
#         print(f"Language {self.lan}")

# class Programmer(Employer, Coder):
#     tech = "Python"
#     def __init__(self, name):
#         self.name = name
#         print(f"constructor of P {self.tech}")


# c = Programmer("Dev")
# c.show()
# c.showLan()

# MULTILEVEL INHERITANCE

# class Employer:
#     company = "MicroSoft"
#     def __init__(self, name):
#         self.name = name
#         print(f"constructor of E {self.company}")
    
#     def show(self):
#         print(f"hello {self.name}")

# class Coder(Employer):
#     lan = "Python"
#     def __init__(self, name):
#         self.name = name
#         print(f"constructor of C {self.lan}")

#     def showLan(self):
#         print(f"Language {self.lan}")

# class Programmer(Coder):
#     tech = "Python"
#     def __init__(self, name):
#         self.name = name
#         print(f"constructor of P {self.tech}")


# d = Programmer("Dev")
# d.show()
# d.showLan()

# SUPER METHOD
# class Employer:
#     company = "MicroSoft"
#     def __init__(self, name):
#         self.name = name
#         print(f"constructor of E {self.company}")
    
#     def show(self):
#         print(f"hello {self.name}")

# class Coder(Employer):
#     lan = "Python"
#     def __init__(self, name):
#         self.name = name
#         super().__init__(name)
#         print(f"constructor of C {self.lan}")

#     def showLan(self):
#         print(f"Language {self.lan}")

# class Programmer(Coder):
#     tech = "Python"
#     def __init__(self, name):
#         self.name = name
#         # Coder.__init__(self, name)
#         super().__init__(name)
#         print(f"constructor of P {self.tech}")


# d = Programmer("Dev")
# d.show()
# d.showLan()

# CLASSMETHOD
# class Employer:
#     company = "MicroSoft"

#     @classmethod
#     def show(cls):
#         print(f"name of E {cls.company}")

# e = Employer()
# print(e.company)
# e.company = "NK"
# print(e.company)
# e.show()

#  PROPERTY | SETTER | GETTER

# class Employer:

#     @property
#     def name(self):
#         return f"Hello Dear,\n {self.fname} {self.lname}"

#     @name.setter
#     def name(self, value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]


# f = Employer()
# f.name = "Dev NK"
# print(f.fname, f.lname)
# print(f.name)               # Output: Dev NK (uses the getter)


# OPERATOR OVERLOADING IN PYTHON

class Calculation:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        return self.num + num2.num

    def __mul__(self, num2):
        return self.num * num2.num

    def __sub__(self, num2):
        return self.num - num2.num

    def __truediv__(self, num2):
        return self.num / num2.num

    def __floordiv__(self, num2):
        return self.num // num2.num
    
    def __str__(self):
        return f"Calculation(num={self.num})"

    def __len__(self):
        return len(str(self.num))

g = Calculation(4)
h = Calculation(2)
print(g + h)
print(g - h)
print(g * h)
print(g / h)
print(g // h)
print(str(g))
print(len(g))
print(str(h))
print(len(h))