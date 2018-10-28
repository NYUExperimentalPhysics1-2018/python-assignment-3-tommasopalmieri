#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests trajectory from tanks.py

@author: gershow
"""

from tanks import trajectory
import matplotlib.pyplot as plt

x,y = trajectory(1,1, 20, 45)
plt.clf()
plt.plot(x,y)
xt = [1, 11.458698248219541, 21.917396496439082, 32.376094744658616,42.792958199885284]
yt = [1,8.778781206560431,11.19772832980265,8.256841369726654,0]
plt.plot (xt,yt,'ko')
plt.title('trajectory should go through black circles')
plt.show()