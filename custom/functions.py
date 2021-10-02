from numpy import *
from math import *


def fourier_series(x, n, a0, a, b):
    y = a0/2
    for i in range(0, n):
        if i < n:
            y += a[i]*cos((i+1)*x) + b[i]*sin((i+1)*x)
        else:
            break
    return y



def quaternion_multiplication(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return np.array([w, x, y, z])






def square_wave(x, n):
    y = 0
    for i in range(1, n):
        y += sin((2*i - 1)*x)/(2*i - 1)
    return y
