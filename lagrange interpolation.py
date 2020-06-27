from numpy import *
from matplotlib import pyplot as plt
##generating points for interpolation(data set can be used instead of known function to get Xi and Yi)
def f(x):
    return 1/(1+x**2)
S=[]
T=[]
Xi=[]
Yi=[]
yo=[]
fi=[]
for i in range(-100,100):
    y=f(i*0.01)
    S.append(y*0.01)
    T.append(i*0.01)
    if i%10==0:
        Xi.append(i*0.01)
        Yi.append(y*0.01)

plt.plot(Xi,Yi,".")
##plt.plot(T,S)
##plt.show()

############
x=linspace(-1,1,1000)
n=len(Yi)

Fi=0
for i in range(0,n):
    pr=1
    for k in range(0,n):
            if k!=i:
                prod=(x-Xi[k])/[Xi[i]-Xi[k]]*pr
                pr=prod
    Fi=Fi+Yi[i]*pr




plt.plot(x,Fi)
plt.show()