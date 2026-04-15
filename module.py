from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

class Model:
    
    def __init__(self, train_data, test_data):
        
        self.train_data = train_data
        self.test_data = test_data
        
    def arima(self, p, d, q):
        
        arima_model = ARIMA(self.train_data, order=(p,d,q))
        model = arima_model.fit()
        num_pred = self.test_data.shape[0]
        y_pred = model.forecast(num_pred)
        
        return y_pred, num_pred
        
    def model2(self):
        pass
    
    def google_model(self):
        pass

class Model_pred:
    def __init__(self, all_data):
        
        self.all_data = all_data

    def best_pred(self, p, d, q):
        arima_model = ARIMA(self.all_data, order=(p,d,q))
        model = arima_model.fit()
        y_pred = model.forecast(1)
        return y_pred