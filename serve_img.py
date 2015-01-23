__author__ = 'kmu'

import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.savefig(r"/home/karsten/mysite/media/test_img.png")