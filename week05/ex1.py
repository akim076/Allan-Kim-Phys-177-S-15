import numpy as np
import math
from pylab import plot, show
import matplotlib
from numpy import linspace
x = linspace(0 ,1, 100)
y = 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

fig= plot(x, y)
show()
accuracy = 1e-10
x = .03
delta = 1.0
while abs(delta) >  accuracy:
	delta =  5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42
	x-=delta
	print(x)
x = .16
delta = 1.0
while abs(delta) > accuracy:
        delta =  5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42
        x-=delta
        print(x)
x = .38
delta = 1.0
while abs(delta) >  accuracy:
        delta =  5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42
        x-=delta
        print(x)
x = .63
delta = 1.0
while abs(delta) > accuracy:
        delta =  5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42
        x-=delta
        print(x)
x = .83
delta = 1.0
while abs(delta) >  accuracy:
        delta =  5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42
        x-=delta
        print(x)
x = .97
delta = 1.0
while abs(delta) >  accuracy:
        delta =  5544*x**5 - 13860*x**4 + 12600*x**3 - 5054*x**2 + 840*x -42
        x-=delta
        print(x)
