import numpy as np


def function(A, x):
    pass  # Define your function. See some examples below.


def linear(A, x):
    return A[1] * x + A[0]


def polynomial(A, x):
    return A[2] * x**2 + A[1] * x + A[0]


def polynomial_n(n):
    def func(A, x):
        return sum([A[i] * (x**i) for i in range(n+1)])

    return func


def optics(A, x):
    return A[1] * x / (x - A[1]) + A[0]


def exponential(A, x):
    return A[2] * np.exp(A[1] * x) + A[0]


def sinusoidal(A, x):
    return A[3] * np.sin(A[1] * x + A[2]) + A[0]


def logarithmic(A, x):
    return A[2] * np.log(A[1] * x) + A[0]


def exponent_sum_n(n):
    def func(A, x):
        return sum([A[i] * np.exp(A[i+1] * x) for i in range(0, n*2, 2)])

    return func
