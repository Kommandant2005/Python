import numpy as np
import matplotlib.pyplot as plt
def function(x, y):
	return np.sin(np.sqrt(x ** 2 + y ** 2))


x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)

X, Y = np.meshgrid(x, y)
Z = function(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, cmap='cool', alpha=0.8)

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_zlabel('z', fontsize=12)
plt.grid(projection="3d")
plt.show()
