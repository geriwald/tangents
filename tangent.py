import matplotlib.pyplot as plt
import numpy as np

l = 4*np.pi
x = np.linspace(-l, l, 1000)
e = np.linspace(-l, l, 2)
dx = x[1]-x[0]
y = np.cos(x) + np.sin(2*x)
d = np.gradient(y, dx)

fig = plt.figure(figsize=(15, 15))

for point in zip(x, y, d):
    X, Y, A = point
    B = Y - A * X
    tangent = A * e + B
    plt.plot(e, tangent, color='k', linewidth=.1)

plt.plot(x, y, color='r', linewidth=2)
plt.ylim([-10, 10])
plt.xlim([-4*np.pi, 4*np.pi])
plt.show()
