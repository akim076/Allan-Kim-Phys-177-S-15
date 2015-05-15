from numpy import loadtxt
from pylab import plot, xlim, show
from numpy import zeros
from cmath import exp, pi
import numpy as np
import pylab
import matplotlib.pyplot as plt
def dft(y):
	N = len(y)
	c = zeros(N//2+1, complex)
	for k in range(N//2+1):
		for n in range(N):
			c[k] +=  y[n]*exp(-2j*pi*k*n/N)
	return c

values = loadtxt("sunspots.txt",float)
months = values[:,0]
sunspots = values[:,1]
plot (months, sunspots)
show()
#estimation cycle length: 131
#b:
c = dft(sunspots)
mag = abs(c)
magSq = mag**2
print len(magSq)
plot (magSq)
pylab.xlabel('k')
pylab.ylabel('magnitude squared coefficiant of sunspots')
show()
#c:aprx value of k = 24
#sine wave:sin ((2pikx)/L)   period =2pi/|B| B=(2*pi*k)/L L =N
B = 0.0
B = (2*pi*24)/len(sunspots)
absB = abs(B)
period = (2*pi)/absB
print period
#period = 131

