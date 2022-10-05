# coding:utf-8
import math

import numpy as np
import matplotlib.pyplot as plt
import math


n = np.linspace(-10, 10, 50)
y1 = 4 * (n ** 2)
y2 = []
for i in n:
    y2.append(math.log2(i))

plt.plot(n, y1)
plt.plot(n, y2)
plt.show()

