# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:01:17 2021

@author: icuev
"""
class Fill_na:
    
    def __init__(self,database):
        self._data=database
        
    def fill(self,listvar):
        df=self._data.copy()
        for i in listvar:
            df[i]=df[i].fillna(df[i].mean(),inplace=True)
        return df

train_data2=Fill_na(train_data2).fill(["height","weight"])
train_data2["height"]