import math
import numpy as np

def sin(x):
	return math.sin(x)
def cos(x):
	return math.cos(x)
def sqrt(x):
	return math.sqrt(x)
def f(x):
	return sin(sqrt(100*x))*sin(sqrt(100*x))
a = 0.0
b = 1.0
e = 0.0
N = 1
h = (b-a)/N
s = f(a) + f(a+h)
trapi1 = s*h*(1.0/2)
print "trapezoidal evaluation for 1 slice:"
print trapi1
print "error of evaluation: "
c = .455832532
print c - trapi1
sum = 0.0		
while True:
	N = N*2
	h = (b-a)/N
	for k in range(1 ,N,2):
		sum+= f(a+k*h)
	I = (1.0/2) *trapi1 + h*sum
	print "trapezoidal evaluation with %s steps" %N
	print I
	e = (1.0/3)*(I-trapi1)
	print "error of evaluation:"
	print e
	if (abs(e)<=.000001) and (e != 0):
		break
	else:     
		trapi1 = I
		sum = 0 
