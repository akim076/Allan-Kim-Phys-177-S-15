import numpy as np
import math
from math import pi
from pylab import imshow,show,colorbar, xlabel, ylabel
x = 0.0
y= 0.0
x1=0.0
x2=0.0
y_=0.0
r1=0.0
r2=0.0
E = .0008854187817
#1m x 1m at points 1cm, so 100x100 total point
# + charge at (45, 50) and - at (55, 50)
matrix = [[0.0 for i in range(101)] for j in range(101)]
for i in range(101):
	for j in range(101):
		x = j
		y = i
		x1= abs(x-45)
		x2= abs(x-55)
		y_ = abs(y-50)
    		r1 =math.sqrt(x1**2+y_**2)
                r2 = math.sqrt(x2**2+y_**2)
		if (r1 == 0):
			matrix[i][j] = .003
		elif (r2==0):
			matrix[i][j] = -.003
		else:
                	phiP = 1.0/(4*pi *E *r1)
                	phiN = -1.0/(4*pi*E*r2)
                	matrix[i][j] =(phiP+phiN)
imshow(matrix, origin="lower")
colorbar()
gx,gy= np.gradient(matrix)
print gx
print gy
Efield = -(gx+gy)
imshow(Efield, origin = "lower")
colorbar()
show()
