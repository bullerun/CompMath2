import math


def f(x: float, n: int):
    if n == 1:
        return 5.74 * x ** 3 - 2.95 * x ** 2 - 10.28 * x - 3.23
    if n == 2:
        return 3 * x ** 3 + 1.5 * x ** 2 - 17 * x + 5.21
    if n == 3:
        return 2 * x ** 3 - 3 * x + 2
    if n == 4:
        return math.cos(x) * math.sin(x) * x
    if n == 5:
        return x ** 2


def first_derivative(x: float, n: int):
    if n == 1:
        return 17.22 * x ** 2 - 5.9 * x - 10.28
    if n == 2:
        return 9 * x ** 2 + 3 * x - 17
    if n == 3:
        return 6 * x ** 2 - 3
    if n == 4:
        return math.cos(2 * x) * x + math.cos(x) * math.sin(x)
    if n == 5:
        return 2 * x


def second_derivative(x: float, n: int):
    if n == 1:
        return 34.44 * x - 5.9
    if n == 2:
        return 18 * x + 3
    if n == 3:
        return 12 * x
    if n == 4:
        return -2 * x * math.sin(2 * x) + 2 * math.cos(2 * x)
    if n == 5:
        return 2
