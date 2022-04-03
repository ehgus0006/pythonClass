import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

plt.style.use('default')
plt.rcParams['figure.figsize'] = (6, 3)
plt.rcParams['font.size'] = 12
plt.rcParams['lines.linewidth'] = 5

mu1, sigma1 = 0.0, 1.0
mu2, sigma2 = 1.5, 1.5
mu3, sigma3 = 3.0, 2.0

x = np.linspace(-8, 8, 1000)
y1 = (1 / np.sqrt(2 * np.pi * sigma1**2)) * np.exp(-(x-mu1)**2 / (2 * sigma1**2))
y2 = (1 / np.sqrt(2 * np.pi * sigma2**2)) * np.exp(-(x-mu2)**2 / (2 * sigma2**2))
y3 = (1 / np.sqrt(2 * np.pi * sigma3**2)) * np.exp(-(x-mu3)**2 / (2 * sigma3**2))

plt.plot(x, y1, alpha=0.7, label=r'PDF of N(0, $1^2$)')
plt.plot(x, y2, alpha=0.7, label=r'PDF of N(1.5, $1.5^2$)')
plt.plot(x, y3, alpha=0.7, label=r'PDF of N(3.0, $2.0^2$)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(bbox_to_anchor=(1.0, -0.2))
plt.show()