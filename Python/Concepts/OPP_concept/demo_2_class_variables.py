
def bad_way():
    class Employee:

        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + "." + last + "@email.com"

        def fullname(self):
            return "{} {}".format(self.first, self.last)

        def apply_raise(self):
            self.pay = int(self.pay * 1.04)

    emp_1 = Employee("Raman", "Sharma", 10000)
    emp_2 = Employee("Rohit", "Kumar", 30000)

    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)


def good_way():
    class Employee:

        raise_amount = 1.04
        num_of_emps = 0

        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + "." + last + "@email.com"

            Employee.num_of_emps += 1

        def fullname(self):
            return "{} {}".format(self.first, self.last)

        def apply_raise(self):
            # self.pay = int(self.pay * Employee.raise_amount)
            self.pay = int(self.pay * self.raise_amount)

    print(Employee.num_of_emps)

    emp_1 = Employee("Raman", "Sharma", 10000)
    emp_2 = Employee("Rohit", "Kumar", 30000)

    # print(emp_1.pay)
    # emp_1.apply_raise()
    # print(emp_1.pay)

    # print(Employee.raise_amount)
    # print(emp_1.raise_amount)
    # print(emp_2.raise_amount)

    # print(Employee.__dict__)
    # print(emp_1.__dict__)

    # Employee.raise_amount = 1.05
    # print(Employee.raise_amount)
    # print(emp_1.raise_amount)
    # print(emp_2.raise_amount)

    # emp_1.raise_amount = 1.05
    # print(Employee.raise_amount)
    # print(emp_1.raise_amount)
    # print(emp_2.raise_amount)

    print(Employee.num_of_emps)



# bad_way()
good_way()
