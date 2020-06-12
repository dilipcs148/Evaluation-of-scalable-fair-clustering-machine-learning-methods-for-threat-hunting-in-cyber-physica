# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 23:13:29 2019

@author: Amin-CSL
"""
import numpy as np
def SWAT2015_getdata():
    filename='Physical_SWAT_2015.npy'
    data=np.load(filename)
    print('Dataset SWAT2015 Loaded')
    datalen=len(data[0])
    X=data[:,0:datalen-2]
    y=data[:,datalen-1]
    return X,y
