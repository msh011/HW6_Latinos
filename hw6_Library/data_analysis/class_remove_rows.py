# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:23:27 2021

@author: icuev
"""
class Preprocessor_Nan:
    def __init__(self,database):
        self._db=database
    def remove_nan(self,listvar):
        df=self._db.dropna(subset=listvar)
        return df        
        
        
