from numpy import *
from matplotlib import pyplot as plt

order=5

T0=[]
Tp=[]
Y=linspace(0,100,100)
##print(Y)

x=linspace(-1,1,100)
print(x)

for i in range(0,100):
    Tm=1/sqrt(pi)
    T0.append(Tm)
##print(T0)

T1=sqrt(2/pi)*x
T2=sqrt(2/pi)*(2*x**2-1)
Tp=[T0,T1,T2]

print(Tp)
for j in range(3,order):
    Tn=2*x*T2-T1
    Tp.append(Tn)
    T1 = T2
    T2 = Tn

print(len(Tp[0]))


for k in range(0,order):
    plt.plot(x,Tp[k])

plt.show()






