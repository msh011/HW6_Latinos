# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 08:00:15 2021

@author: icuev
"""

import pandas as pd
from sklearn.model_selection import train_test_split

class load_split_data:
    
    def __init__(self,filename):
        self.filename=filename
        self._data=None
        
    def read_data(self):        
        try:
            self._data=pd.read_csv(str(self.filename))
            return self._data
        except FileNotFoundError:
            return "File not found. Does the file exist?" 
        
    
    def split_data(self,test_size):
        data_train,data_test=train_test_split(self._data, test_size=0.2, random_state=42)
        return data_train,data_test

class read_split_data:
    
    def __init__(self,filename):
        self.filename=filename
        self._data=None
        
    def read_split(self,test_size):        
        try:
            self._data=pd.read_csv(str(self.filename))
        except FileNotFoundError:
            return "File not found. Does the file exist?" 
        
        data_train,data_test=train_test_split(self._data, test_size=0.2, random_state=42)
        
        return data_train,data_test
