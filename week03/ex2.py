import numpy as np
import math
from numpy import array, empty
from numpy.linalg import solve

#V1:  4V1 - V2 - V3 - V4 = V+
#V2:  -V1 + 3V2 -0  - V4 = 0
#V3:  -V1 + 0 + 3V3 - V4 = V+
#V4:  -V1 - V2 - V3 + 4V4 = 0

#Ax = v
A = array([[ 4, -1, -1, -1 ],
	   [-1,  3,  0, -1 ],
	   [-1,  0,  3, -1 ],
	   [-1, -1, -1,  4 ]], float)

v = array([ 5, 0, 5, 0], float)
N = len(v)

for m in range(N):
	div = A[m,m]
	A[m,:] /= div
	v[m] /= div
	for i in range(m+1, N):
		mult = A[i, m]
		A[i, :] -= mult*A[m,:]
		v[i] -= mult*v[m]
x = empty (N, float)
for m in range(N-1, -1, -1):
	x[m] = v[m]
	for i in range(m+1, N):
		x[m] -= A[m,i]*x[i]
print(x)
x = solve(A, v)
print (x)
