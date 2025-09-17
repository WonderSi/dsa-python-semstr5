import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3, 4, 1000)
y = x**2 - x - 6

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, label="y(x) = x^2 - x - 6", color="blue", linewidth=2)

ax.axhline(0, color='gray', linestyle='--', linewidth=1)

roots = [-2, 3]
ax.scatter(roots, [0, 0], color='red', zorder=5, label='Roots $y=0$')

ax.set_title("y(x) = x^2 - x - 6")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)

plt.show()
