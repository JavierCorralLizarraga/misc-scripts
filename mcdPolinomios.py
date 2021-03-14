# -*- coding: utf-8 -*-

from sympy import div
from sympy.abc import x

# Algoritmo de euclides para obtener el máximo común divisor entre dos polinomios
def mcdPoli(a, b):
    if b == 0:
        return a
    else:
        q, r = div(a, b)
        print("(" + str(a) + ") = (" + str(q) + ") * (" + str(b) + ") + (" + str(r) + ")")
        return mcdPoli(b, r)

a = x**2 + 1
b = 2*x - 4
print(mcdPoli(a,b))
