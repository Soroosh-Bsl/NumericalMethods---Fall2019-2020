import numpy as np

print("Enter f -> y' = f(x, y):")
input_function = input()
print("Enter h:")
h = float(input())
print("Enter x0 and y0 respectively:")
x0, y0 = map(float, input().split())
print("Enter the required x")
x_target = float(input())


def heun(f, h, x_target, x_start, y_start):
    n = int((x_target - x_start) // h)
    for i in range(n):
        k1 = h * f(x_start, y_start)
        k2 = h * f((x_start+2/3*h), (y_start+2/3*k1))
        y_start = y_start + 0.25 * (k1 + 3*k2)
        x_start += h
    return y_start


def f(x, y):
    """The input function can only have 'e' from special symbols, sin or cos or ... are not accepted!"""
    global input_function
    replaced = str(input_function).replace('x', str(x))
    replaced = str(input_function).replace('y', str(y))
    replaced = replaced.replace('e', str(np.math.e))
    return eval(replaced)


print("The y at the point", x_target, "is", heun(f, h, x_target, x0, y0))