import matplotlib.pyplot as plt
import numpy as np

l = 10*np.pi
x = np.linspace(-l, l, 1000)
e = np.linspace(-l, l, 2)
dx = x[1]-x[0]
y = np.cos(x)/x

d = np.gradient(y, dx)

fig = plt.figure(figsize=(70, 15))
ax = plt.axes()
ax.set_facecolor('k')

for point in zip(x, y, d):
    X, Y, A = point
    B = Y - A * X
    tangent = A * e + B
    plt.plot(e, tangent, color='dimgray', linewidth=.05)


#plt.plot(x, y, color='r', linewidth=2)
plt.xlim([-l, l])
plt.ylim([-2, 2])
plt.savefig('screen.png')
plt.show()
