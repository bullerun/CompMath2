from functions import *
from prettytable import PrettyTable
from system import system_of_equations


def check_interval(a: float, b: float, fun_num: int) -> bool:
    if f(a, fun_num) * f(b, fun_num) < 0:
        if first_derivative(a, fun_num) * first_derivative(b, fun_num) >= 0:
            return True
        return False
    return False


def chord_method(fun_num: int, interval: tuple, eps: float):
    a = interval[0]
    b = interval[1]
    x = 100
    x_prev = 0
    table = PrettyTable()
    table.field_names = ["№ шага", "a", "b", "x", "f(a)", "f(b)", "f(x)",
                         f"|x{chr(0x2096)}{chr(0x208A)}{chr(0x2081)} - x{chr(0x2096)}|"]
    i = 1
    while abs(x - x_prev) > eps:
        x_prev = x
        x = a - (b - a) / (f(b, fun_num) - f(a, fun_num)) * f(a, fun_num)
        table.add_row([i, a, b, x, f(a, fun_num), f(b, fun_num), f(x, fun_num), abs(x - x_prev)])
        if f(a, fun_num) * f(x, fun_num) < 0:
            b = x
        if f(b, fun_num) * f(x, fun_num) < 0:
            a = x
        i += 1
    res = {
        "i": i,
        "x": x,
        "f(x)": f(x, fun_num),
        "table": table.get_string()
    }
    return res


def newtons_method(fun_num: int, interval: tuple, eps: float):
    table = PrettyTable()
    table.field_names = ["№ шага", f"x{chr(0x2096)}", f"f(x{chr(0x2096)})", f"f'(x{chr(0x2096)})",
                         f"x{chr(0x2096)}{chr(0x208A)}{chr(0x2081)}",
                         f"|x{chr(0x2096)}{chr(0x208A)}{chr(0x2081)} - x{chr(0x2096)}|"]
    a = interval[0]
    b = interval[1]
    if f(b, fun_num) * second_derivative(b, fun_num) > 0:
        x = b
    else:
        x = a
    x_prev = x + eps + 1000
    i = 1
    while abs(x - x_prev) > eps:
        x_prev = x
        x = x_prev - f(x_prev, fun_num) / first_derivative(x_prev, fun_num)
        table.add_row([i, x_prev, f(x_prev, fun_num), first_derivative(x_prev, fun_num), x, abs(x - x_prev)])
        i += 1
    res = {
        "i": i,
        "x": x_prev,
        "f(x)": f(x_prev, fun_num),
        "table": table.get_string()
    }
    return res


def simple_iteration_method(fun_num: int, interval: tuple, eps: float):
    table = PrettyTable()
    table.field_names = ["№ итерации", f"x{chr(0x2096)}", f"x{chr(0x2096)}{chr(0x208A)}{chr(0x2081)}",
                         f"f(x{chr(0x2096)}{chr(0x208A)}{chr(0x2081)})",
                         f"|x{chr(0x2096)}{chr(0x208A)}{chr(0x2081)} - x{chr(0x2096)}|"]
    a = interval[0]
    b = interval[1]
    my_lambda = -1 / max(first_derivative(a, fun_num), first_derivative(b, fun_num))
    last_x = 1
    if f(a, fun_num) * second_derivative(a, fun_num) > 0:
        last_x = a
    elif f(b, fun_num) * second_derivative(b, fun_num) > 0:
        last_x = b
    start_x = last_x + my_lambda * f(last_x, fun_num)
    i = 1
    q = max(abs(1 + my_lambda * first_derivative(a, fun_num)), abs(1 + my_lambda * first_derivative(b, fun_num)))
    if q > 1:
        return {"error": "Нет сходимости"}
    while abs(start_x - last_x) > eps or f(last_x, fun_num) < eps:
        table.add_row([i, last_x, start_x, f(start_x, fun_num), abs(start_x - last_x)])
        last_x = start_x
        start_x = last_x + my_lambda * f(last_x, fun_num)
        i += 1
    table.add_row([i, last_x, start_x, f(start_x, fun_num), abs(start_x - last_x)])
    res = {
        "i": i,
        "x": last_x,
        "f(x)": f(last_x, fun_num),
        "table": table.get_string()
    }
    return res


def get_solution(fun_num: int, interval: tuple, eps: float, method: int, in_file: bool):
    if method == 1:
        return preparing_to_send(chord_method(fun_num, interval, eps), in_file)
    elif method == 2:
        return preparing_to_send(newtons_method(fun_num, interval, eps), in_file)
    elif method == 3:
        return preparing_to_send(simple_iteration_method(fun_num, interval, eps), in_file)
    elif method == 4:
        return preparing_to_send_system(system_of_equations(fun_num, interval, eps), in_file)


def preparing_to_send_system(a, in_file):
    if in_file:
        with open("1.txt", "w", encoding="utf-8") as f:
            f.writelines(f"Количество итераций: {a["i"]}\n")
            f.writelines(f"Корень {a["x"]}\n")
            f.writelines(f"Значение функции в точке корня {a["y"]}\n\n")
            f.writelines(f"Дельта {a["delta"]}")
    else:
        return a


def preparing_to_send(a: dict, in_file: bool):
    if "error" in a:
        if in_file:
            with open("1.txt", "w", encoding="utf-8") as f:
                f.writelines(f"{a["error"]}")
        else:
            return a
    else:
        if in_file:
            with open("1.txt", "w", encoding="utf-8") as f:
                f.writelines(f"Количество итераций: {a["i"]}\n")
                f.writelines(f"Корень {a["x"]}\n")
                f.writelines(f"Значение функции в точке корня {a["f(x)"]}\n\n")
                f.writelines(a["table"])
        else:
            a.pop("table")
            return a
