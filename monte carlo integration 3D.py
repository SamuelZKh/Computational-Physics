from numpy import *
from matplotlib import pyplot as plt
import random

from mpl_toolkits.mplot3d import axes3d
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
X=[]
Y=[]
Z=[]
Sum=0
Vol=(4*pi/3)
N=50000
def f(x,y,z):
    return x**2+y**2+z**2
for i in range(0,N):
    x=random.randint(0,100)/100
    y=random.randint(0,100)/100
    z=random.randint(0,100)/100

    Integral=f(x,y,z)
    if (Integral<1):

        Sum = Integral + Sum
        I=Sum/N
        X.append(x)
        Y.append(y)
        Z.append(z)

print(I)
ax.scatter(X,Y,Z)               ###ax.scatter can be used for a scatter plot
plt.show()













