from functools import reduce
""" anonymous functions
lambda always return list
syntax lambda [x1,x2,x,3..xn] : expression
"""


def build_quadratic_function(a, b, c):
    """returns the function f(x) = ax^2  bx + c"""
    return lambda x: a * x ** 2 + b * x + c


f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

print(build_quadratic_function(3, 0, 1)(2))  # 3x^2+1 evaluate ofr x = 2

# filters
n = [4, 3, 2, 1]
print(list(filter(lambda x: x > 2, n)))

n = [1, 2, 3, 4]
print(reduce(lambda x, y: x * y, n))
