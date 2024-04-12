import numpy as np
import math


def system_newton(system, initial_guess, eps):
    max_iterations = 100
    x = initial_guess
    iteration = 0
    while iteration < max_iterations:
        f = np.array([eq(*x) for eq in system])
        J = np.array(
            [[partial_derivative(system[i], j, x[0], x[1]) for j in range(len(x))] for i in range(len(system))])
        delta_x = np.linalg.solve(J, -f)
        x += delta_x
        iteration += 1
        if np.linalg.norm(delta_x) < eps:
            break
    res = {
        "i": iteration,
        "x": x[0],
        "y": x[1],
        "delta": np.linalg.norm(delta_x)
    }
    return res


def partial_derivative(f, var_index, *args):
    h = 1e-6
    args_list = list(args)
    args_list[var_index] += h
    f_plus_h = f(*args_list)
    args_list[var_index] -= 2 * h
    f_minus_h = f(*args_list)
    return (f_plus_h - f_minus_h) / (2 * h)


def system_of_equations(fun_num, initial_guess, eps):
    if fun_num == 1:
        return system_newton([lambda x, y: x ** 2 + y ** 2 - 4, lambda x, y: 3 * x ** 2 - y], initial_guess, eps)
    if fun_num == 2:
        return system_newton([lambda x, y: math.sin(x) + 2 * y - 2, lambda x, y: x + math.cos(y - 1) - 0.7],
                             initial_guess, eps)
    if fun_num == 3:
        return system_newton([lambda x, y: x ** 4 + y ** 4 - 1, lambda x, y: x - y], initial_guess, eps)
