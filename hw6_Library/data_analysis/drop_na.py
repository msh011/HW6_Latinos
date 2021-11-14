# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:52:23 2021

@author: icuev
"""
def drop_na_rows(data,list_var):
    data=data.dropna(subset=list_var)
    return data