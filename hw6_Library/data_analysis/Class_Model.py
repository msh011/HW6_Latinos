from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self, regressors, target, C=100):
        self._regressors=regressors #List with the features that we want to use to predict.
        self._target=target # Variable that we want to predict
        self._C=C## We will ask for the hyperparameter C
        self.model= LogisticRegression(penalty='l2', C=self._C, 
                           fit_intercept=True, 
                           intercept_scaling=1, 
                           solver='liblinear', max_iter=500)
    
    def train(self,train_data):
        x = train_data[self._regressors]
        y = train_data[self._target]
        self.model.fit(x,y)
        
    def predict(self,df):
        x = df[self._regressors]
        prob_pred = self.model.predict_proba(x)
        return prob_pred #The output is the probabilitie of 0 and the probabilite of 1 for the variable of interest



