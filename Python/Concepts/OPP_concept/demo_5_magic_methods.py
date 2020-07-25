class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname} - {self.pay}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Raman", "Sharma", 10000)
emp_2 = Employee("Rohit", "Kumar", 10000)

print(emp_1)

# Checking repr and str dunder method
print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())


# checking add dunder method
print(emp_1 + emp_2)
print(emp_1.__add__(emp_2))


# checking len dunder method
print(len(emp_1))
