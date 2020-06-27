import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import *
##plt.style.use('fivethirtyeight')
L=5
X=[]
Y=[]
                             ###### function to find fs of##############
def g(x):
    if abs(x)<2:
        return 5
    if abs(x)>=2:
        return 0
        #################################### a,an,bn  ###################
def a(a,b):
    def f(x):
        return g(x)
    n = 5000
    I = 0
    J = 0
    h = (b - a) / n
    for j in range(1, n + 1):
        if j % 2 == 0:
            J = J + f(a + j * h)
        else:
            I = I + f(a + j * h)
    Int = (h / 3) * (f(a) + f(b) + 2 * I + 4 * J)
    return Int
def an(a,b,n):
    def f(x):
        return g(x)*cos((n*x*pi)/L)
    N = 5000
    I = 0
    J = 0
    h = (b - a) / N
    for j in range(1, N + 1):
        if j % 2 == 0:
            J = J + f(a + j * h)
        else:
            I = I + f(a + j * h)
    Int = (h / 3) * (f(a) + f(b) + 2 * I + 4 * J)
    return Int
def bn(a,b,n):
    def f(x):
        return g(x)*sin((n*pi*x)/L)
    N = 5000
    I = 0
    J = 0
    h = (b - a) / N
    for j in range(1, N + 1):
        if j % 2 == 0:
            J = J + f(a + j * h)
        else:
            I = I + f(a + j * h)
    Int = (h / 3) * (f(a) + f(b) + 2 * I + 4 * J)
    return Int

for i in range(-L,L):
    X.append(i)
    Y.append(g(i))
plt.plot(X,Y)
plt.show()

ai = []
x = linspace(-L, L, 3000)
for i in range(0, len(x)):
    ai.append(a(-L, L))
##print(ai,len(ai))

index = count(1)


def animate(i):
    n=next(index)
    asum = 0
    bsum = 0
    for j in range(0, n):
        asum = asum + an(-L, L, j) * cos((j * pi * x))
    for j in range(0, n):
        bsum = bsum + bn(-L, L, j) * sin((j * pi * x))

    y = ((a(-L,L) / 2) + asum + bsum) /L
    plt.cla()
    plt.plot(x,y)
    print(y,len(y),"y")
    print(x,"x")

ani = FuncAnimation(plt.gcf(),animate,interval=1000)  ##get current figgure ## 10000=1 sec  as interval decreases time decreases
plt.tight_layout()
plt.show()












