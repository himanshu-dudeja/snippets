# Property decorator helps us to define a method which we can use as an attribute.

def basic_example_of_property_decorator():
    class Employee:

        def __init__(self, first, last):
            self.first = first
            self.last = last
            # self.email = first + "." + last + "@email.com"

        def fullname(self):
            return "{} {}".format(self.first, self.last)

        @property
        def email(self):
            return f'{self.first}.{self.last}@email.com'

    emp_1 = Employee("Raman", "Sharma")

    emp_1.first = 'Aman'

    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.fullname())


def advanced_example_of_property_decorator():
    class Employee:

        def __init__(self, first, last):
            self.first = first
            self.last = last

        @property
        def fullname(self):
            return "{} {}".format(self.first, self.last)

        @fullname.setter
        def fullname(self, name):
            first, last = name.split()
            self.first = first
            self.last = last

        @fullname.deleter
        def fullname(self):
            print('Delete Name')
            self.first = None
            self.last = None

        @property
        def email(self):
            return f'{self.first}.{self.last}@email.com'

    emp_1 = Employee("Raman", "Sharma")

    emp_1.fullname = 'Aman Kumar'

    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.fullname)

    del emp_1.fullname


# basic_example_of_property_decorator()
advanced_example_of_property_decorator()
