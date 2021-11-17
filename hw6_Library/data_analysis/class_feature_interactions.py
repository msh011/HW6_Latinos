# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:34:12 2021

@author: Stefan Hoeller
"""

class Interactions():
    
   
    def __init__(self,data):
        self.data=data

        
    def create_interactions(self,listvar):
        #Create polynomials for columns from 2 till degree specified
        for i in listvar:
            for j in listvar:
                if i!=j:
                    self.data[i+"_"+j]=self.data[i]*self.data[j]
                
        return self.data

