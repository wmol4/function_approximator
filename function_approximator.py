import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV

test_array = np.array([[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36]]) #a test dataset representing y = x^2

X_data = test_array.T[0].reshape(test_array.shape[0], 1)
y_data = test_array.T[1]

params = {'kernel': ['rbf', 'linear', 'poly', 'sigmoid'], 'degree': [1, 2, 3, 4], 'C': [0.01, 0.1, 1], 'gamma': [1]}
classifier = GridSearchCV(model, params) #gridsearchCV searching through the above parameters
classifier.fit(X_data, y_data) #fit to the data
best_params = classifier.best_params_ #find the best parameters

model = SVR(degree = best_params['degree'], kernel = best_params['kernel'], C = best_params['C'], gamma = best_params['gamma']) #initialize a SVR model (support vector regression)

model.fit(X_data, y_data)

print(model.predict(np.array([[7]]))) #prints ~48.83
