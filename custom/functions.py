from numpy import *
from math import *
import os



def get_image(filename):
    dir = "Images"
    file = os.path.join(dir, filename)
    return file



def get_portrait(filename):
    dir = "Images/Portraits"
    file = os.path.join(dir, filename)
    return file



def get_svg(filename):
    dir = "SVG"
    file = os.path.join(dir, filename)
    return file



def get_sound(filename):
    dir = "Sound"
    file = os.path.join(dir, filename)
    return file



def get_norm(vect):
    return sum((x**2 for x in vect))**0.5



def C(n, k):
    """
    C(n, k) = n! / (n - k)! k!
    """
    c = 1

    if (k > n - k):
        k = n - k
    for a in range(0, k):
        c = c * (n - a)
        c = c // (a + 1)
    
    return c



def F(N):
    """
    Fibonacci Sequence.
    F(n + 1) = F(n) + F(n - 1)
    """
    a = 0
    b = 1
    F = [a, b]
    for j in range(1, N + 1):
        c = a + b
        a = b
        b = c
        F.append(c)
    
    return F[N]



def quaternion_multiplication(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return np.array([w, x, y, z])



def fourier_series(x, n, a0, a, b):
    y = a0/2
    for i in range(0, n):
        if i < n:
            y += a[i]*cos((i+1)*x) + b[i]*sin((i+1)*x)
        else:
            break
    return y



def square_wave(x, n):
    y = 0
    for i in range(1, n):
        y += sin((2*i - 1)*x)/(2*i - 1)
    return y
