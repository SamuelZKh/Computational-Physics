from numpy import *
from matplotlib  import pyplot as plt
import random

h_bar=6.582*10**-16 # eV-s
m_0=6*10**-32 #kg
cons=(2*m_0/(h_bar**2))**0.5



# Number of Potential Barrier (PB)
k=2

# For potential Heights
v=[0.0]
for i in range(1,2*k+2):
    r=random.randint(0,5)
    if(i%2==0):
        v.append(r)
    else:
        v.append(0.0)

# For potential width and intermediate space between two PBs
x_breaks=[0.0]
for i in range(1,2*k+2):
    if(i%2!=0.0):
        int_gap= x_breaks[i-1]+4.0   # intermediate distance b/w two PBs (taken 4 nm here)
        x_breaks.append(int_gap)
    else:
        width=x_breaks[i-1]+4.0 # intermediate distance b/w two PBs (taken 4 nm here)
        x_breaks.append(width)
print(len(v))
print(len(x_breaks))
print(v)
print(x_breaks)
plt.plot(x_breaks, v)
plt.show()

k=[]
for i in range(len(v)):




