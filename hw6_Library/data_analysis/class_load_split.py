# -*- coding: utf-8 -*-
"""

"""
class Df_load():
    
   
    def __init__(self,filepath):
        data=Df_load.read_data(filepath)
        self.train, self.test=Df_load.split_data(data)
        
    def read_data(namefile):
        import pandas as pd
        try:
            data=pd.read_csv(namefile)
            return data
        except NameError:
            print("\n","NameError occurred. Some variable isn't defined.")
    
    
    
    def split_data(data):
        from sklearn.model_selection import train_test_split
        data_train,data_test = train_test_split(data, test_size=0.2, random_state=42)
        return data_train,data_test
    
