import numpy as np
import math
from pylab import plot, xlim, show
from cmath import exp, pi
from numpy import zeros
from scipy import signal
N = 1000
def dft(y): 
	N = 1000
	c = zeros(N//2 + 1, complex)
	for k in range(N//2 +1):
		for n in range(N):
			c[k] += y[n]*exp(-2j*pi*k*n/N)
	return c
#a: single cycle of square  wave with amp 1 
t = np.linspace(0, 2, 1000, endpoint=False)
y = signal.square(2*pi*t)
c = dft(y)
plot(abs(c))
xlim(0,500)
show()


#b: sawtooth wave y_n=n
y = range(1000)
#x = range(1000)
c = dft(y)
plot(abs(c))
xlim(0, 500)
show()

#c: modulated sine wave y_n=sin(pi*n/N)*sin(20*pi*n/N)
y=zeros(1000, float)
for i in range(1000):
	y[i] = math.sin(pi*i/N) * math.sin(20*pi*i/N)
c = dft(y)
plot(abs(c))
xlim(0,500)
show()
	
