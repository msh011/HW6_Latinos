# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:50:40 2021

@author: icuev
"""
import pandas as pd

def read_data(namefile):
    try:
        data=pd.read_csv(namefile)
        return data
    except NameError:
        print("\n","NameError occurred. Some variable isn't defined.")
