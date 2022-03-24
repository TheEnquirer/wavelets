import numpy as np
import scipy
import math

e = math.e

def phi(A, t, s, c):
    if c:
        return (A*e**((-t**2)/2)) * (e ** (1j * s * t)) - (e ** ((-s**2)/2))
    return (A*e**((-t**2)/2)) * (e ** (-1j * s * t)) - (e ** ((-s**2)/2))

def inner_product(func, j, k):
    return 2**(j/2) * scipy.integrate.quad(phi(1, x*2**j, 1, 0)*func, 0, 1)


def testfunct():
    return x**2

inner_product(testfunct, 0, 0)












