def f1(x):
    return x**2


def f2(x):
    return x**3+5*x**2-19


def find_solution(function, n_repeat, x_now, x_prev):
    x_next = None
    for i in range(n_repeat):
        "To prevent division by zero 1e100 is added."
        x_next = x_now - (function(x_now)*(x_now - x_prev))/(function(x_now)-function(x_prev)+1e-100)
        x_prev = x_now
        x_now = x_next
        print("x"+str(i+1)+" =", x_now)
    print("The final answer is", str(x_now))
    print("f(answer) =", function(x_now))
    return x_now


find_solution(f1, 10, 1, 2)
find_solution(f2, 20, 0.6, 1.9)