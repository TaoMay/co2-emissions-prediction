import pandas as pd
import numpy as np

class Dataset:
    
    def __init__(self, csv_path):
        self.csv_path = csv_path


    def read_csv(self):
        cvs_df = pd.read_csv(self.csv_path, names = ['year','month','decimal date',"average","deseasonalized","ndays","sdev", 'unc'], header = None, skiprows=41)

        cvs_arr = np.array(cvs_df)
        
        header_dict = {}
        for idx, each in enumerate(cvs_df.columns.values):
            header_dict[each] = idx
       
        return cvs_arr, header_dict

    
    def split_configuration(self, year_split):
        
        cvs_arr, header_dict = self.read_csv()

        train_idx = np.where(cvs_arr[:, header_dict['decimal date']] < year_split)[0]
        test_idx = np.where(cvs_arr[:, header_dict['decimal date']] >= year_split)[0]
        
        # x_train = cvs_arr[train_idx, header_dict['year']]
        train_data = cvs_arr[train_idx, header_dict['average']]
        
        # x_test = cvs_arr[test_idx, header_dict['year']]
        test_data = cvs_arr[test_idx, header_dict['average']]
        
        all_data = all_data = np.concatenate([train_data, test_data])
        return train_data, test_data, all_data
 
        

if __name__ == "__main__":
    cvs_path  = 'co2_mm_mlo.csv'
    
    dataset = Dataset(cvs_path)
    a, b, c = dataset.split_configuration(2024)