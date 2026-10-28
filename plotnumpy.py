import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("x**2")
plt.grid()
plt.show()
