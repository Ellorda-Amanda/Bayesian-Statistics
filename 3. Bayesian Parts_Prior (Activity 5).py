# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 20:12:08 2024

@author: Abalora, Dellavan, Ellorda, Esclamado
"""

import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(1.65, 1.8, num = 50)
test = np.linspace(0, 2)

uniform_dist = sts.uniform.pdf(mu) + 1 #for clarity

uniform_dist = uniform_dist/uniform_dist.sum() #probability density into 1

beta_dist = sts.beta.pdf(mu, 2, 5, loc = 1.65, scale = 0.2)
beta_dist = beta_dist/beta_dist.sum()
plt.plot(mu, beta_dist, label = 'Beta Dist')
plt.plot(mu, uniform_dist, label = 'Uniform Dist')
plt.xlabel("Value of $\mu$ in meters")
plt.ylabel("Probability density")
plt.legend()


