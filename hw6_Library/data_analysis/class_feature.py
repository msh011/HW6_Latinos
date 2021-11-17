# -*- coding: utf-8 -*-
"""

"""

from abc import ABCMeta, abstractmethod
class Feature(metaclass=ABCMeta):    
    def __init__(self,data):
        self.data=data
    
    @abstractmethod
    def create_feature(self):
        return NotImplementedError
    
    


class Polys(Feature):
    
        
    def create_feature(self,listvar,degree=3): #give a list of variables
        #Create polynomials for columns from 2 till degree specified
    
        for i in listvar:
            counter=2
            while counter<=degree:
                self.data[i+'_'+str(counter)]=self.data[i]**counter
                counter+=1
        return self.data
    
class Interactions(Feature):

        
    def create_feature(self,listvar):
        #Create polynomials for columns from 2 till degree specified
        for i in listvar:
            for j in listvar:
                if i!=j:
                    self.data[i+"_"+j]=self.data[i]*self.data[j]
                
        return self.data
  
    

    
    
