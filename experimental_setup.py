import pandas as pd
import os

extension = 'csv'
os.chdir(os.getcwd())

#read base_data.csv
base_data = pd.read_csv("input/creditcard.csv")

#sample base_data into training_data and test_data
training_data = base_data.sample(frac=0.8,random_state=200) #TODO adjust random_state
test_data = base_data.drop(training_data.index)
#sample training_data into training_data_minority
training_data_minority = training_data[training_data['Class'] == 1]

#create folder for .csv
if(os.path.isdir('results') == False):
    os.mkdir("results")

#create .csv for each data set
base_data.to_csv("results/base_data.csv", index=False)
training_data.to_csv("results/training_data.csv", index=False)
test_data.to_csv("results/test_data.csv", index=False)
training_data_minority.to_csv("results/training_data_minority.csv", index=False)