from data_preprocess import *
from module import *
from evaluation import *
import matplotlib.pyplot as plt

def Model_Choose(cvs_path):
    
    dataset = Dataset(cvs_path)
    # TODO: Year_Split need to be experimented
    train_data, test_data, all_data = dataset.split_configuration(2024.2)

    # TODO: Add more models
    model = Model(train_data, test_data)
    y_pred, num_pred = model.arima(2,1,2)

    metric = Metric(y_pred, test_data)
    result = metric.mse()
    
    print(y_pred)
    print(num_pred)
    print("MSE:", result)

    best_model = Model_pred(all_data)
    April_pred = best_model.best_pred(2,1,2)
    print(April_pred)

if __name__ == "__main__":
    
    cvs_path  = 'co2_mm_mlo.csv'
    Model_Choose(cvs_path)
    