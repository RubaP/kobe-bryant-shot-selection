import pandas as pd 

data = pd.read_csv('data/data.csv')

print("Sperating training and test data")
predicting_set = data.loc[data['shot_made_flag'].isnull() , :]
training_data = data.loc[ data['shot_made_flag'].notnull() , :]
predicting_set.to_csv('data/test_set.csv')
training_data.to_csv('data/training_set.csv')# -*- coding: utf-8 -*-
print("Training data set size: ", training_data.shape)
print("Sperating training and test data", predicting_set.shape)
