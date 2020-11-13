import numpy as np


def gauss_sidel_completely(A, X, b, epsilon):

    def gauss_seidel(A, X, b):
        n = len(A)
        for j in range(0, n):
            tmp = b[j]
            for i in range(0, n):
                if i != j:
                    tmp -= A[j][i] * X[i]
            X[j] = tmp / A[j][j]
        return X

    A = np.asarray(A)
    X = np.asarray(X)
    b = np.asarray(b)
    for i in range(0, 25):
        prev_x = X.copy()
        X = gauss_seidel(A, X, b)
        print("Step {}:\n".format(i)+str(X))
        # Check if error is less than epsilon
        if np.max(np.abs(prev_x-X)) < epsilon:
            break
    print("Final result with error less than {}\n".format(epsilon) + str(X))


print("Enter number of unknowns:")
n = int(input())
A = []
print("Enter A (each row of matrix in a row):")
for i in range(n):
    tmp = list(map(float, input().split()))
    A.append(tmp)
print("Enter b (separated by space):")
b = list(map(float, input().split()))
print("Enter X_initial (separated by space):")
X = list(map(float, input().split()))
print("Enter epsilon (maximum ERROR)")
epsilon = float(input())

gauss_sidel_completely(A, X, b, epsilon)






