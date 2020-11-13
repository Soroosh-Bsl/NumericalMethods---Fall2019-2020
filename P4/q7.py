import numpy as np

print("Enter a and b:")
a, b = map(float, input().split(' '))
print("Enter the pdf function:")
input_function = input()
print("Enter n:")
n = int(input())
random_numbers = []


def f(x):
    """The input function can only have 'e' from special symbols, sin or cos or ... are not accepted!"""
    global input_function
    replaced = str(input_function).replace('x', str(x))
    replaced = replaced.replace('e', str(np.math.e))
    return eval(replaced)


def integral_calc(x):
    """Calculating integral of function f in [a, x]"""
    global a, b, f
    h = (x-a)/10
    integ = 0.
    for i in range(11):
        integ += 2*f(a+h*i)
    integ -= (f(a)+f(x))
    integ *= h/2
    return integ


def produce_number(uniform_num):
    global a, b, f
    new_a = a
    new_b = b
    current_guess = (a+b)/2
    while True:
        integ = integral_calc(current_guess)
        if uniform_num + 1e-10 >= integ >= uniform_num - 1e-10:
            return current_guess
        elif uniform_num > integ:
            new_a = current_guess
            current_guess = (current_guess + new_b)/2
        else:
            new_b = current_guess
            current_guess = (new_a + current_guess)/2


def produce_for_all():
    global a, b, f, n, random_numbers
    for i in range(n):
        uniform_num = np.random.uniform(0., 1.)
        random_numbers.append(produce_number(uniform_num))
    for x in random_numbers:
        print(x, end=' ')


produce_for_all()
