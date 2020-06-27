from numpy import *
from matplotlib import pyplot as plt
##for copper
s=0.385
p=8.96
K=5.96*10**7
L=1
c=K/(s*p*L*L)

##initialising variables
Ti0=1
T1=0
T2=10

N=10

yi=0
yf=1
dy=(yf-yi)/N
a=0.3
dt=a*dy**2
Tn=0

Tn=[]
Y=[]
t=[]
T=zeros([T2,N])

for time in range(0,T2):
    for i in range(0, N ):
        if i == 0:
            T[time, i] = T1
        if i != 0:
            T[time, i] = 5
        if i == N-1:
            T[time, i] = T2


for time in range(0,T2-1):
    for j in range(1, N-1):
       T[time+1,j] = (a * T[time,j - 1] + (1 - 2 * a) * T[time,j] + a * T[time,j + 1])




for y in range(0,N):

    yi=yi+dy
    Y.append(yi)


for time in range(0, T2):

    tempPLot = T[time]
    print(tempPLot)
    print(Y)
    plt.plot(tempPLot,Y)


plt.show()










