# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:53:41 2021

@author: icuev
"""
from sklearn.linear_model import LogisticRegression 
def train_and_predict_log(train_data,test_data,list_var_X,y="diabetes_mellitus"):
    X=train_data[list_var_X]
    X_test=test_data[list_var_X]
    y=train_data[y]
    lregr = LogisticRegression(penalty='l2', C=100.0, 
                           fit_intercept=True, 
                           intercept_scaling=1, 
                           solver='liblinear', max_iter=500)
    lregr.fit(X,y)
    y_prob_train=lregr.predict_proba(X)
    train_data["predicted_y_train"]=y_prob_train[:,1]
    
    y_prob_test=lregr.predict_proba(X_test)
    test_data["predicted_y_test"]=y_prob_test[:,1]
    
    return train_data,test_data,y_prob_train,y_prob_test