# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:51:48 2021

@author: icuev
"""
from sklearn.model_selection import train_test_split

def split_data(data):
    data_train,data_test=train_test_split(data, test_size=0.2, random_state=42)
    return data_train,data_test