import math


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


def calc_sin_using_taylor(angle):
    angle = float(angle)
    i = 0
    result = 0.
    while True:
        result += ((-1)**(i) * (angle)**(2*i+1))/fact(2*i+1)
        i += 1
        if abs((angle)**(2*i+1)/fact(2*i+1)) < 0.001:
            break
    return result


x = input('Enter the angle in radian: ')
res = calc_sin_using_taylor(x)
print("Calculated sin using taylor expansion =", res)
print("The error from the real value =", abs(math.sin(float(x))-res), "< 10^-3")
