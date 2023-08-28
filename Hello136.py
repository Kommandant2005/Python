import numpy as np
import matplotlib.pyplot as plt
f
R = 2

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(-1, 1, 100)
u, v = np.meshgrid(u, v)
x = (R + v*np.cos(u/2)) * np.cos(u)
y = (R + v*np.cos(u/2)) * np.sin(u)
z = v * np.sin(u/2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Möbius Strip')

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

plt.show()
