from pylab import *
from cmath import *

n = 3

A = zeros((n, n), dtype=complex)
Q, R = zeros((n, n), dtype=complex), zeros((n, n), dtype=complex)

for i in range(0, n):
    for j in range(0, n):
        r = randint(-10, 10)
        c = randint(-10, 10)
        A[i][j] = complex(r, c)

K = A
m = 0

while m < 200:
    for i in range(0, n):
        u = K[:, i]
        for j in range(0, i):
            u = u - dot(u, conj(Q[:, j])) * Q[:, j]
        Q[:, i] = u / sqrt(dot(u, conj(u)))

    R = dot(Q.transpose(), conj(K))

    K = dot(R, conj(Q))
    m = m + 1

for i in range(0, n):
    print("eigenvalue", str(i + 1), "=", K[i][i].round(decimals=4))

print(eigvals(A).round(decimals=4))
