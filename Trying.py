#print("hello world")
""""
Create a new file namedknn.py(you might want to use PyCharm).
2 Inside the file create a class named KNN that can take differentparameters as input (e.g k, distance, etc.).  
Create theinitfunction to initialise the instances of your class;
3Create a fit function that takes as input the X 2-D array of training data and y 1-D array of training labels and 
processes this data to train the model;
4Create a predict function that takes as input the X 2-D array of testing data and output the y 1-D array of predicted labels for the testing data
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import math
import operator
#TRAIN AND TEST SPLIT DATA 
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

class KNN:
	def __init__(self):
        pass 

    def fit(self, x, y):
		self.x_train = x
		self.y_train = y

	def predict(self, x, y):
		self.x_test = x
		self.y_test = y

	def euclidean_distance(v1, v2, length):
    for x in range(length):
        distance = pow((v1[x]-v2 [x]), 2)
    return math.sqrt(distance)
	
	def closest_neighbors (x_train, x_test, k):
    distances = []
    neighbors = []
    for i in range(0, x_train.shape[0]):
        dist = euclidean_distance(X_train[i], x_test)
        distances.append((i, dist))
    distances.sort(key=operator.itemgetter(1))
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors



"""KNN(X_train, X_test, Y_train, Y_test, k):
    output_classes = []
    for i in xrange(0, X_test.shape[0]):
        output = get_neighbours(X_train, X_test[i], k)
        predictedClass = predictkNNClass(output, Y_train)
        output_classes.append(predictedClass)
    return output_classes
"""
"""
import KNN
X =[[0], [1], [2], [3]] y =[0, 0, 1, 1]
knn =KNN(k=3) 
knn.fit(X, y) 
predicted_labels = knn.predict([[1.1]]) 
print(predicted_labels)
"""

