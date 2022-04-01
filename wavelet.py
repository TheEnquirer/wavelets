import numpy as np
import scipy
import math
from scipy import integrate
import sympy as sym
from sympy.plotting import plot
import cmath
e = math.e
j=[0]
k=[0]
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

def rSq(functionInp, functionTest):
    ar1 = []
    ar2 = []
    for i in np.arange(0.0, 1, 0.1):
        ar1.append(functionInp.evalf(subs={'x': i}))
        ar2.append(functionTest.evalf(subs={'x': i}))
    currErr = 0
    for i in range(len(ar1)):
        print(ar1[i])
        print(ar2[i])
        currErr += (ar2[i]-ar1[i])**2
    # print(cmath.sqrt(currErr/len(ar1)))
    return cmath.sqrt((currErr/len(ar1)))
# p1 = plot(real(runExpansion(j, k)), show = False)
#p2 = plot(testfunct, show = False)
#p1.append(p2[0])
# p1.show()

rSq(runExpansion(j, k), testfunct())













