import numpy as np
from sklearn.metrics import mean_squared_error

class Metric:
    def __init__(self, y_pred, y_true):
        self.y_pred = y_pred
        self.y_true = y_true
    
    def mse(self):
        result = mean_squared_error(self.y_pred, self.y_true)
        
        return result
    
    
    def idk(self):
        pass
    

if __name__ == "__main__":
    a = np.array([2.5, 3.7, 4.2, 5.0, 6.1])
    b = np.array([2.2, 3.5, 4.0, 4.8, 5.8])
    metric = Metric(b,a)
    result = metric.mse()
    print(result)
        