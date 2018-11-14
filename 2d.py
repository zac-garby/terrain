import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import math

magnitude_range = (-1, 1)
x_scale_range = (-5, 5)
phase_range = (-5, 5)
wave_num = 500

waves = []

for i in range(wave_num):
    waves.append((random.uniform(*magnitude_range),
                  random.uniform(*x_scale_range),
                  random.uniform(*phase_range)))

def wave_function(x):
    result = 0

    for wave in waves:
        result += wave[0] * math.sin(wave[1] * x + wave[2])

    return result

wave_function = np.vectorize(wave_function)

t = np.arange(-100, 100, 0.01)
s = wave_function(t)

fig, ax = plt.subplots()
ax.plot(t, s)
ax.grid()
fig.savefig("test.png")
plt.show()


