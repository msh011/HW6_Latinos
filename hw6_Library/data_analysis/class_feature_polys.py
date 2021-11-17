# -*- coding: utf-8 -*-
"""

"""
class Polys():
    
   
    def __init__(self,data):
        self.data=data

        
    def create_poly(self,listvar,degree=3): #give a list of variables
        #Create polynomials for columns from 2 till degree specified
    
        for i in listvar:
            counter=2
            while counter<=degree:
                self.data[i+'_'+str(counter)]=self.data[i]**counter
                counter+=1
        return self.data
    
  
    

    
    
