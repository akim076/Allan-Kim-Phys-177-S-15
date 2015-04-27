import math
from ex1 import trapR, simpR
import numpy as np
from numpy import array

def f(x):#for intrinsic functions I think
        return x**4-2*x+1
#using my functions (it needs 21 x inputs and f(x))
x_ = [0.0]
y_ = []
for k in range(1,21):
	s =  k*.1
	x_.append(s)
for i in range(0,21):
	c = x_[i]
	d = f(c)
	y_.append(d)	
print "trapezoidal evaluation using functions:"
print trapR(x_, y_)

print "Simpson's evaluation using functions:"
print simpR(x_, y_)

s = 0
N = 20
a = 0.0
b = 2.0
h = (b-a)/N
s = .5*f(a) + .5*f(b)
for k in range (1,N):
	s += f(a+k*h)
print "intrinsic function of trapezoidal:"
print (h*s)
trapIN = h*s
s = 0
oddk = 0.0
evenk=0.0
for k in range (1,N,2):
	oddk += f(a+k*h)
for k in range (2,N,2):
	evenk+= f(a+k*h)
s = f(a) + f(b) +4*oddk + 2*evenk
simpIN  = 1.0/3.0* h * s
print "intrinsic function of Simpson's:"
print simpIN

#work for error
s = 0
x__ = [0.0]
y__ =[]
for k in range(1,11):
	s= k*.2
	x__.append(s)
for i in range(0, 11):
	c= x__[i]
	d = f(c)
	y__.append(d)
I_1trap = trapR(x__, y__)
I_1simp = simpR(x__, y__)
print "trapezoidal N=10: "
print  I_1trap
print "simpsons N=10: "
print  I_1simp
print "error of trapezoidal N=20:"
print 1/3.0*(trapIN - I_1trap)
print "error of simpsons N=20:"
print 1/15.0*(simpIN - I_1simp)
print "true integral:"
c = 4.4
print c
print "true integral - trapezoidal(N=20) ="
print (c - trapIN)
print "true integral - simpsons(N=20) ="
print (c - simpIN) 
