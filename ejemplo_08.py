a#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:35:26 2019

@author: mar
"""
#Modelo de una neurona artificial
import numpy as np
x = np.array([0.0,0.5,0.3,-0.7])
w = np.array([-0.6,0.7,0.2,-0.1])
y = np.dot(x,w)

np.tanh(y)
1/1+exp(-y)