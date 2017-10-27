#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:12:11 2017

@author: altron01
"""

import numpy as np
from matplotlib import pyplot as plt
import cv2
import os
import time

def clean(img, size):
    for i in range(size[0]):
        for j in range(size[1]):
            img[i][j] = (255 if img[i][j] > 70 else 0)
    pass

def dilatarImg(img):
    size = img.shape
    container = np.copy(img)
    center = (3, 3)
    mask = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i in range(size[0]):
        for j in range(size[1]):
            if img[i][j] == 0:
                for y in range(mask.__len__()):
                    di = i + y - center[0]
                    for x in range(mask[0].__len__()):
                        dj = j + x - center[0]
                        if (0 <= di < size[0]) and(0 <= dj < size[1]):
                            if mask[y][x] == 0:
                                container[di][dj] = 0
    plt.imshow(cv2.cvtColor(container, cv2.COLOR_GRAY2RGB))
    plt.show();
    pass

def erosionImg(img):
    size = img.shape
    container = np.copy(img)
    center = (0, 1)
    mask = [[0, 255]]
    for i in range(size[0]):
        for j in range(size[1]):
            if img[i][j] == 0:
                for y in range(mask.__len__()):
                    di = i + y - center[0]
                    for x in range(mask[0].__len__()):
                        dj = j + x - center[0]
                        if (0 <= di < size[0]) and(0 <= dj < size[1]):
                            if img[di][dj] != mask[y][x]:
                                container[di][dj] = 255
    plt.imshow(cv2.cvtColor(container, cv2.COLOR_GRAY2RGB))
    plt.show()
    pass

img = cv2.imread("img2.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
plt.show()
clean(img, img.shape)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_GRAY2RGB))
plt.show()
dilatarImg(img)
erosionImg(img)