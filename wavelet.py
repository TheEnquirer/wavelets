import numpy as np
import scipy
import math
from scipy import integrate
import sympy as sym
e = math.e
j=[0, 1]
k=[0, -1, 1]
def phi(A, t, s, c):
    if c:
        return (A*e**((-t**2)/2)) * (e ** (1j * s * t)) - (e ** ((-s**2)/2))
    return (A*e**((-t**2)/2)) * (e ** (-1j * s * t)) - (e ** ((-s**2)/2))

def inner_product(func, j, k):
    x=sym.Symbol('x')
    return 2**(j/2) * sym.integrate(phi(1, x*2**j, 1, 0)*func, (x, 0, 1))


def testfunct():
    x=sym.Symbol('x')
    return x**2
def runExpansion(arrJ, arrK):
    currsum = 0
    x=sym.Symbol('x')
    for p in range(len(arrJ)):
        for q in range(len(arrK)):
            currsum += 2**(arrJ[p]/2)*phi(1, x*2**arrJ[p], 1, 1)*inner_product(testfunct(), arrJ[p], arrK[q])
    return currsum
print(runExpansion(j, k))
