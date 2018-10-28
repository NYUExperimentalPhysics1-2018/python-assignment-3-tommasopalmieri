#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test tankshot and drawboard from tanks.py
requires completion of both of these items

@author: gershow

"""

from tanks import tankShot
from tanks import drawBoard
import matplotlib.pyplot as plt

tank1box = [10,15,0,5]
tank2box = [90,95,0,5]
obstacleBox = [40,60,0,50]

plt.figure(1)
drawBoard(tank1box,tank2box,obstacleBox,1)
hit = tankShot(tank2box, obstacleBox, 12.5,2.5,100,70)
plt.title ('a shot that goes over the target')
if hit:
    print ('you incorrectly detected a hit -1')

plt.figure(2)
drawBoard(tank1box,tank2box,obstacleBox,1)
hit = tankShot(tank2box, obstacleBox, 12.5,2.5,100,60)
plt.title ('a shot that hits the obstacle')
if hit:
    print ('you incorrectly detected a hit -2 ')

plt.figure(3)
drawBoard(tank1box,tank2box,obstacleBox,1)
hit = tankShot(tank2box, obstacleBox, 12.5,2.5,150,89)
plt.title ('a high arcing kill shot!')
if hit:
    print ('you correctly detected a hit')
else:
    print ('you incorrectly reported a miss -3')
