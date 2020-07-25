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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):

        # Both these are same
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)

        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('----->', emp.fullname())


emp_1 = Developer("Raman", "Sharma", 10000, "Python")
emp_2 = Employee("Rohit", "Kumar", 10000)

# print(emp_1.email)
# print(emp_2.email)

# This is very helpful for understanding the underlying methods and variables.
# print(help(Developer))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.prog_lang)

# print("-----------")

# print(emp_2.pay)
# emp_2.apply_raise()
# print(emp_2.pay)


mgr_1 = Manager('Aman', "Deep", 90000, [emp_1])
# print(mgr_1.email)
# mgr_1.print_emps()
# mgr_1.add_emp(emp_2)
# mgr_1.print_emps()


def check_isinstance():
    # Using isinstance
    print(isinstance(mgr_1, Manager))
    print(isinstance(mgr_1, Employee))
    print(isinstance(mgr_1, Developer))


def check_issubclass():
    # Using issubclass
    print(issubclass(Manager, Employee))
    print(issubclass(Developer, Employee))
    print(issubclass(Developer, Manager))


# check_isinstance()
# check_issubclass()
