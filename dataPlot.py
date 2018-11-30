#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:45:56 2018

@author: liguo
"""

import numpy as np
import matplotlib.pyplot as plt

# Hill Climbing data

# Best successor
# 9*9
simple2_0 =  np.array([[0.0269889831543, 0.0210738182068, 0.0254490375519, 0.040195941925]])
simple2_1 = np.array([[0.0391039848328, 0.0223798751831, 0.0238790512085, 0.0355310440063]])
simple2_2 = np.array([[0.0745677947998, 0.0770859718323, 0.076290845871, 0.0634069442749]])
simple2_3 = np.array([[2.94567513466, 2.82208919525, 4.54819011688, 1.81693601608]])
simple2_4 = np.array([[]])

data = np.concatenate((simple2_0.T, simple2_1.T, simple2_2.T, simple2_3.T), 1)
print data
fig1, ax1 = plt.subplots()
ax1.set_title('Steepest Acsent Hill Climbing(9*9)')
ax1.boxplot(data)

# 4 * 4
simple_0 = np.array([[0.00650501251221, 0.012039899826, 0.00640082359314, 0.005774974823]])
simple_1 = np.array([[0.025120973587, 0.0302770137787, 0.0391111373901, 0.0273420810699]])
simple_2 = np.array([[0.0467238426208, 0.0872540473938, 0.256032943726, 0.530433893204]])
simple_3 = np.array([[0.128174066544, 0.0327930450439, 0.0387780666351, 0.0587818622589]])
simple_4 = np.array([[0.0354709625244, 0.0495710372925, 0.0290508270264, 0.0327370166779]])

data = np.concatenate((simple_0.T, simple_1.T, simple_2.T, simple_3.T, simple_4.T), 1)
print data
fig1, ax1 = plt.subplots()
ax1.set_title('Steepest Acsent Hill Climbing(4*4)')
ax1.boxplot(data)


# First Successor
# 9*9
simple2_0 = np.array([[ 0.0306029319763, 0.019681930542, 0.0222079753876, 0.0218741893768]])
simple2_1 = np.array([[ 0.0334420204163, 0.0310080051422, 0.0240390300751, 0.0369670391083]])
simple2_2 = np.array([[ 0.349719047546, 0.954236984253, 0.247157096863, 0.664642095566]])
simple2_3 = np.array([[]])
simple2_4 = np.array([[]])
data = np.concatenate((simple2_0.T, simple2_1.T, simple2_2.T), 1)
print data
fig1, ax1 = plt.subplots()
ax1.set_title('Simple Hill Climbing(9*9)')
ax1.boxplot(data)

# 4*4
simple_0 = np.array([[0.00966119766235, 0.0121788978577, 0.00708389282227, 0.0100300312042]])
simple_1 = np.array([[ 0.158025026321, 0.292256832123, 0.528688907623, 0.0728278160095]])
simple_2 = np.array([[ 2.75815296173, 0.188815832138, 1.67441511154, 0.32562494278]])
simple_3 = np.array([[ 0.337473154068, 4.34701800346, 0.716123104095, 4.00713920593]])
simple_4 = np.array([[ 0.78049993515, 2.97117209435, 0.599956989288, 2.93151807785]])

data = np.concatenate((simple_0.T, simple_1.T, simple_2.T, simple_3.T, simple_4.T), 1)
print data
fig1, ax1 = plt.subplots()
ax1.set_title('Simple Hill Climbing(4*4)')
ax1.boxplot(data)


















