# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:53:09 2021

@author: icuev
"""
import pandas as pd
def dummies(data,list_var):
    for i in list_var:
        data=pd.get_dummies(data,prefix=[i],columns=[i],drop_first=True)
    return data