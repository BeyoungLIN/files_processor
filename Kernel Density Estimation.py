import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
from sklearn.neighbors.kde import KernelDensity
a = np.array([45, 51, 52, 53, 53, 54, 55, 62, 64, 72, 77, 77, 77, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81]).reshape(-1, 1)
kde = KernelDensity(kernel='gaussian', bandwidth=3).fit(a)
s = np.linspace(0, 115)
e = kde.score_samples(s.reshape(-1, 1))
plt.plot(s, e)
plt.show()
mi, ma = argrelextrema(e, np.less)[0], argrelextrema(e, np.greater)[0]
print("Minima:", s[mi])
print("Maxima:", s[ma])
print(a[a < mi[0]], a[(a >= mi[0]) * (a <= mi[1])], a[a >= mi[1]])
plt.plot(s[:mi[0] + 1], e[:mi[0] + 1], 'r',
         s[mi[0]:mi[1] + 1], e[mi[0]:mi[1] + 1], 'g',
         s[mi[1]:], e[mi[1]:], 'b',
         s[ma], e[ma], 'go',
         s[mi], e[mi], 'ro')
plt.show()