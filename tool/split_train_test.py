#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import os
import re
import random
import shutil
random.seed(2)
import sys

pathX='C:\\Users\\heca0002\\Desktop\\train_new2'
pathY='C:\\Users\\heca0002\\Desktop\\label_new3'
out_x='C:\\Users\\heca0002\\Desktop\\val_x'
out_y='C:\\Users\\heca0002\\Desktop\\val_y'
ratio=0.18



X_train_files = os.listdir(pathX)
X_train_files.sort()
Y_train_files = os.listdir(pathY)
Y_train_files.sort()



data = list(zip(X_train_files, Y_train_files))


random.shuffle(data)
X_train_files[:], Y_train_files[:] = zip(*data)


if len(X_train_files)==len(Y_train_files):
    print('pass')
else:
    print('file number mismatch')
    sys.exit()

offset = int(len(Y_train_files) * ratio)
val_file_x = X_train_files[:offset]
val_file_y = Y_train_files[:offset]

for i in val_file_x:
    shutil.move(pathX + '/' + i, out_x)

for j in val_file_y:
    shutil.move(pathY + '/' + j, out_y)







