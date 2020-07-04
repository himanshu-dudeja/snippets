
def employee_example():
    def add_employee(emp, emp_list=[]):
        emp_list.append(emp)
        print(emp_list)

    emp_list = ['ABC', 'PQR']

    # # This seems to be fine
    add_employee("MNR", emp_list)

    # # This will have a wired o/p
    print(add_employee.__defaults__)
    add_employee("AAA")
    print(add_employee.__defaults__)
    add_employee("BBB")
    print(add_employee.__defaults__)
    add_employee("CCC")
    print(add_employee.__defaults__)
    # output
    # ['AAA']
    ## ['AAA', 'BBB']
    ## ['AAA', 'BBB', 'CCC']

    # In python default args are evaluated once at the time it created the function

    def add_employee_fixed(emp, emp_list=None):
        if emp_list is None:
            emp_list = []
        emp_list.append(emp)
        print(emp_list)

    print(add_employee_fixed.__defaults__)
    add_employee_fixed("AAA")
    print(add_employee_fixed.__defaults__)
    add_employee_fixed("BBB")
    print(add_employee_fixed.__defaults__)
    add_employee_fixed("CCC")
    print(add_employee_fixed.__defaults__)


def datetime_example():
    import time
    from datetime import datetime

    def display_time(time_to_print=datetime.now()):
        print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))

    print(display_time.__defaults__)
    display_time()
    print(display_time.__defaults__)
    time.sleep(1)
    display_time()
    print(display_time.__defaults__)
    time.sleep(1)
    display_time()
    print(display_time.__defaults__)
    time.sleep(1)

    def display_time_fixed(time_to_print=None):
        if time_to_print is None:
            time_to_print = datetime.now()
        print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))

    print(display_time_fixed.__defaults__)
    display_time_fixed()
    print(display_time_fixed.__defaults__)
    time.sleep(1)
    display_time_fixed()
    print(display_time_fixed.__defaults__)
    time.sleep(1)
    display_time_fixed()
    print(display_time_fixed.__defaults__)
    time.sleep(1)


if __name__ == '__main__':
    # employee_example()
    # datetime_example()
