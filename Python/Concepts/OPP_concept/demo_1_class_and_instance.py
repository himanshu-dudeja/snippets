# Python Object Oriented Programming

# A class is basically a blue print for creating instances(objects)
# An each unique employee we create in this class will be an instance of the class.

def bad_way():
    class Employee:
        pass

    emp_1 = Employee()
    emp_2 = Employee()

    print(emp_1)
    print(emp_2)

    emp_1.first = 'ABC'
    emp_1.last = 'PQR'
    emp_1.email = 'ABC.PQR@email.com'
    emp_1.pay = 50000

    emp_2.first = 'MNQ'
    emp_2.last = 'PRT'
    emp_2.email = 'MNQ.PRT@email.com'
    emp_2.pay = 50000

    print(emp_1.email)
    print(emp_2.email)


# bad_way()


def good_way():

    class Employee:

        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + "." + last + "@email.com"

        def fullname(self):
            return "{} {}".format(self.first, self.last)

    emp_1 = Employee("Rocky", "Singh", 50000)
    emp_2 = Employee("Aman", "Sharma", 40000)

    print(emp_1.email, emp_1.fullname())
    print(emp_2.email, emp_2.fullname())

    # These both are same things
    print(emp_1.fullname())
    print(Employee.fullname(emp_1))


good_way()
