# acceleration due to gravity
import math
y0 = 20 # m
v0 = 5 # m/s
g = 9.81 # m/s^2
t = 10 # s
def free_fall(y0, v0, g, t):
  y = y0 + v0*t - 0.5*g**2 
  return(y)
print(free_fall(y0, v0, g, t))
