# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:52:48 2021

@author: icuev
"""
def fillna_avg(data,list_var):
    for i in list_var:
        data[i].fillna(data[i].mean(),inplace=True)
    return data