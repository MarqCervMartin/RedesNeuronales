#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:11:44 2019

@author: mar
#instalar torchvision
pip install torchvision
"""
import numpy as np
import torch

import matplotlib.pyplot as plt

from torchvision import datasets, transforms

#convierte imagenes a tensores
transform = transforms.Compose([transforms.ToTensor(),
                                 transforms.Normalize((0,5),(0,5)),
                                 ])

trainsets = datasets.MNIST('~/.pytorch/MNIST_data/',download = True, train = True,
                                                      transform = transform)
trainloader = torch.utils.data.DataLoader(trainset,batch_size=64,shuffle=True)









