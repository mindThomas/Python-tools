import math
from TIPE import start

class X:

    coeff = 0.5
    def get(t):
        return (X.coeff*math.cos(t)*t, X.coeff*math.sin(t)*t, X.coeff*((t-5)))


start(X)