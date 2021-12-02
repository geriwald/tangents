import matplotlib.pyplot as plt
import numpy as np

l = 4*np.pi
x = np.linspace(-l, l, 1000)
e = np.linspace(-l, l, 2)
dx = x[1]-x[0]
y = x**4 + x**3 - 2 * x**2
d = np.gradient(y, dx)

fig = plt.figure(figsize=(15, 15))

for point in zip(x, y, d):
    X, Y, A = point
    B = Y - A * X
    tangent = A * e + B
    plt.plot(e, tangent,  color='k', linewidth=.1)


#plt.plot(x, y, color='r', linewidth=2)
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.savefig('poly.png')
plt.show()
