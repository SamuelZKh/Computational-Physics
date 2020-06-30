from numpy import *
from matplotlib import pyplot as plt

N=50
x0=-2*pi
xn=2*pi
L=xn-x0
x=linspace(x0,xn,N)
print('X vslue',x)
h=L/N

def signal(x):
    if x >-2 and x<2:
        return 5
    else:
        return 0
y=[signal(i) for i in x]
print('y values',y)
#print(len(x),len(y))
plt.plot(x,y)
plt.show()
print(y)
Ck=[]
for k in range(-(N-1),N-1):
    sum=0
    for i in range(0,N-1):
        temp=y[i] * (exp( complex( 0 , (-2 * pi * i * k) / N)))
        sum=sum+temp
    Ck.append(sum/N)

Cksq=[]
print(Ck)
for i in range(0,len(Ck)):
    Cksq.append(Ck[i]*Ck[i].conjugate())

print('CKsq',Cksq)
k=linspace(-(N-1),N-1,len(Cksq))
plt.plot(k,Cksq)
plt.show()