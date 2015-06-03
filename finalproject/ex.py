from numpy import math
import numpy as np
from math import pi,sin,cos,exp
from numpy import arange, array
from pylab import plot, xlabel, ylabel,show
#a Starting from Newton's 2nd law derive position of x and y
'''
f of air resistance in opposite direction of motion = 1/2*pi*R^2*d*k*v^2
where d is density of air and k is coefficient of darg
let 1/2*pi*R^2*d*k = D
f = Dv^2
where v^2 = sqrt(v_x^2+v_y^2)
direction of f is opposite of v so:
f_x = -D*v*v_x       f_y = -D*v*v_y
now with Force of the cannonball F=ma
F in x direction = -D*v*v_x = ma     F in the y direction = -mg -D*v*v_y = ma
v = sqrt(v_x^2+v_y^2)
a_x (2nd derivative of x component) = -(pi*R^2*d*k)/(2m)*v_x*sqrt(v_x^2+v_y^2) 
a_y (2nd derivative of y component) = -g -(pi*R^2*d*k)/(2m)*v_y*sqrt(v_x^2+v_y^2)
'''

#b Using Runge Kutta method to determine realistic motion with&without air resistance with given values

m = 1.0 #kg
r = .08 #m
theta = 30.0 #from horizantal
v = 100 #initial velocity at m/s
g = 9.8 #m/s^2
C = 0.47 #coefficient of drag
p = 1.22 #kgm^-3 density of air
D = .5 * pi * r^2 * p * C 
def fx(x, t):
	X = r[0]
	Vx= r[1]
	X = Vx
	Vx= -D/m * vx *sqrt(vy^2 + vx^2)
	return array([fX ,fVx] , float)
def fy(y, t):
	Y = z[0]
	Vy= z[1]
	Y = Vy
	Vx= -D/m * vx *sqrt(vy^2+vx^2)-g
	return array([fY , fVy], float)
a = 0.0
b = 900
N = 1000
h = (b-a)/N	
upoints = arange(a, b, h)
xpoints = []
ypoints = []
r = array([0.0], float)
z = array([0.0], float)
for t in tpoints:
	xpoints.append(r[0])
	k1 = h*fx (r,t)
	k2 = h*fx(r+0.5 *k1, t+0.5*h)
	k3 = h*fx(r+0.5*k2, t+0.5*h)
	k4 = h*fx(r+k3, t+h)
	r += (k1+ 2* k2 +2*k3+k4)/6
for t in tpoints:
        ypoints.append(z[0])
        k1 = h*fy (r,t)
        k2 = h*fy(r+0.5 *k1, t+0.5*h)
        k3 = h*fy(r+0.5*k2, t+0.5*h) 
        k4 = h*fy(r+k3, t+h)
        z += (k1+ 2* k2 +2*k3+k4)/6 
plot(xpoints, ypoints)
xlabel ("horizontal")
ylabel ("vertical")
show() 
