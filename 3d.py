import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import random
import math

magnitude_range = (-1, 1)
scale_range = (-5, 5)
phase_range = (-5, 5)
wave_num = 20

waves = []

for i in range(wave_num):
    waves.append((random.uniform(*magnitude_range),
                  random.uniform(*scale_range),
                  random.uniform(*scale_range),
                  random.uniform(*phase_range)))

@np.vectorize
def wave_function(x, y):
    result = 0

    for wave in waves:
        result += wave[0] * math.sin(wave[1] * x + wave[2] * y + wave[3])

    return result / len(waves)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
x, y = np.meshgrid(x, y)
z = wave_function(x, y)

ax.plot_surface(x, y, z, rstride=10, cstride=10, cmap=matplotlib.cm.coolwarm)
plt.show()
