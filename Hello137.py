from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
	return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-1, 5, 10)
y = np.linspace(-1, 5, 10)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)


ax = plt.axes(projection ='3d')
fig = plt.figure()
ax.plot_wireframe(X, Y, Z, color ='green')

