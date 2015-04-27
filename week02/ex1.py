import numpy as np
import math
from numpy import array
def trapR(x, y):
        N= len(x)
        Integral = y[0]/2+y[N-1]/2 + np.sum(y[1:N -1])
        h = x[1]-x[0]
        return (Integral * h)

def simpR (x, y):
        odd = 0
	even= 0
	if len(x)%2 != 1:
                return 'There must be even number of steps'
        else:
                a = x[0]
                N = len(x)-1
                h = x[1]-x[0]
                for k in range (1, N, 2):
                        odd  += y[k]
                for k in range (2, N, 2):
			even += y[k]
                Integral = y[0] + y[N] + 4*odd + 2*even
        return (1/3.0 * h* Integral)
                

