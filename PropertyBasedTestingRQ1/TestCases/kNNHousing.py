
#Importing necessary files
import import_ipynb
import pandas as pd
import csv as cv
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import time


def func_main():
	#Defining the results array which ´will contain execution time and non-monotonicity score
	resultArr = np.zeros((2, ))

	#Reading the dataset
	df = pd.read_csv('Datasets/HousingData.csv') 
	
	fileData = open('DataFile.txt', 'w')
	fileData.write('Datasets/HousingData.csv')
	fileData.close()
	
	#Applying monotonicity constraints
	fileMon = open('monFeature.txt', 'w')
	fileMon.write('RM \nRAD \nTAX')
	fileMon.close()

	data = df.values

	X = data[:, :-1]
	Y = data[:, -1]
	model = KNeighborsClassifier(n_neighbors=3, weights='uniform')

	#Fitting the model with the dataset
	model = model.fit(X, Y)
	

	
	return model


