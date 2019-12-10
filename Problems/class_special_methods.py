""" Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method nam
"""


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    @property
    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr_(self):
        return "Employee('{}', '{}', '{}".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)


emp_1 = Employee('a', 'p', 5000)
print(emp_1)
print(emp_1.fullname)
emp_2 = Employee('b', 'g', 6000)
