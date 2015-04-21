import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import array
from numpy import*
homeWork =np.array( [10, 10, 8, 9.5, 3, 9, 0, 6],float)
midTerm =np.array( [10, 10, 10, 10, 8, 5, 10, 7],int)
Fproject=np.array( [9, 10, 10, 6, 10, 6, 8, 9],int)
grade = homeWork * .4 + midTerm * .2 + Fproject * .4
for n in range(0,8):
	print grade[n]
failed = 0
outstanding = 0
for n in range(0,8): 
	if (grade[n] < 6):
		failed = failed + 1
	elif (grade[n] >9.5):
        	outstanding = outstanding +1
fractionOfOutstanding = outstanding/8.0
print "number of students that failed:"
print failed
print "fraction of outstanding students"
print fractionOfOutstanding
bins=[50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
plt.hist(grade, bins=8, range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype=u'bar', align=u'mid', orientation=u'vertical', rwidth=None, log=False, color=None, label=None, stacked=False, hold=None)
plt.show()
savefig(foo.png)
