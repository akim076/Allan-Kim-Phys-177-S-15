import numpy as np 
import math

h = 800 #height
g = 9.81
v_0 = float(input("What is the initial velocity thrown towards the ground?(in meters):"))
v_fSquared= v_0**2 + 2*g*h
v_f = math.sqrt(v_fSquared)
t = 2*h/(v_0+v_f)
print "Time it takes for ball to reach the ground(in seconds): "
print (t)    
