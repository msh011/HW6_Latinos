# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:12:51 2021

@author: icuev
"""
from sklearn.metrics import roc_auc_score
def roc_auc(data,name_var,pred_prob):
    score=roc_auc_score(data[name_var], pred_prob[:, 1])
    return score