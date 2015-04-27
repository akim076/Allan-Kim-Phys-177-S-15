
import math
from ex1 import trapR, simpR
import numpy as np
from numpy import loadtxt
values = loadtxt("velocities.txt", float)
time = values[:,0]
velocity = values[:,1]
a= trapR(velocity, time)
print a
b= simpR(velocity, time)
distanceT=[0]
print b
displacement = 0.0
for i in range(0,100):
	tempx = [velocity[i], velocity[i+1]]
	tempy = [time[i], time[i+1]]
	displacement += trapR(tempx, tempy)
	distanceT.append(displacement)
z = len(distanceT)
print distance

