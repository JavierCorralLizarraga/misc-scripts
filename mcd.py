# -*- coding: utf-8 -*-
# Algoritmo para obtener el máximo común divisor
def mcd(a, b):
    if b == 0:
        return a
    else:
        q = a // b
        r = a % b
        print(str(a) + " = " + str(q) + " * " + str(b) + " + " + str(r))
        return mcd(b, r)
    
print(mcd(34131, 1984))
