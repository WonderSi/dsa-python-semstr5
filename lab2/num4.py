import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-20,20,1000)

log_base = 1 + np.tan(1 / (1 + np.sin(x)**2))
log_part = np.log(x**2 + 1) / np.log(log_base)
exp_part = np.exp(-np.abs(x) / 10)
y = log_part * exp_part

plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
