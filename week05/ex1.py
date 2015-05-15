import numpy as np
import math
from pylab import plot, show
import matplotlib
from numpy import linspace
z = 0
xA= 0.0
#use eq 6.96 x-x'=error
def f(x):
	z= 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1
	return z
x = linspace(0 ,1, 100)
y = 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

fig= plot(x, y)
show()
accuracy = 1e-10
x = .03
xder = 0.0
delta = 1.0
error = 1.0
while abs(error) >  accuracy:
	xdelta =f(x) /( 5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42)
	xder = x - xdelta
	error = x - xder
	xA = x
	x = xder
print xA
	
x = .16
xder = 0.0
delta = 1.0
error = 1.0
while abs(error) >  accuracy:
        xdelta =f(x) /( 5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42)
        xder = x - xdelta
        error = x - xder
        xA = x
        x = xder
print xA
x = .38
xder = 0.0
delta = 1.0
error = 1.0
while abs(error) >  accuracy:
        xdelta =f(x) /( 5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42)
        xder = x - xdelta
        error = x - xder
        xA = x
        x = xder 
print xA
x = .63
xder = 0.0
delta = 1.0
error = 1.0
while abs(error) >  accuracy:
        xdelta =f(x) /( 5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42)
        xder = x - xdelta
        error = x - xder
        xA = x
        x = xder 
print xA
x = .83
xder = 0.0
delta = 1.0
error = 1.0
while abs(error) >  accuracy:
        xdelta =f(x) /( 5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42)
        xder = x - xdelta
        error = x - xder
        xA = x
        x = xder 
print xA
x = .97
xder = 0.0
delta = 1.0
error = 1.0
while abs(error) >  accuracy:
        xdelta =f(x) /( 5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42)
        xder = x - xdelta
        error = x - xder
        xA = x
        x = xder 
print xA
