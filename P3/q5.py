import matplotlib.pyplot as plt

x_is = [2, 4.25, 5.25, 7.81, 9.2, 10.6]
y_is = [7.2, 7.1, 6, 5, 3.5, 5]


def lagrange(xs):
    ys = [0. for i in range(len(xs))]
    for k in range(len(xs)):
        result = 0.
        for i in range(len(x_is)):
            y = 1
            for j in range(len(x_is)):
                if i != j:
                    y *= (xs[k] - x_is[j])/(x_is[i] - x_is[j])
            result += y_is[i] * y
        ys[k] = result
    return ys


step = (max(x_is) - min(x_is)) / 1000
x_interpolation = []
for i in range(1000):
    x_interpolation.append(min(x_is)+step*i)
plt.plot(x_interpolation, lagrange(x_interpolation))
plt.scatter(x_is, y_is)
plt.title("The path")
plt.show()
