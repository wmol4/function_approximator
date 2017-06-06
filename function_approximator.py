import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.kernel_ridge import KernelRidge

def predict_degrees(x, y):
    """
    predict how many degrees are represented by polynomial data
    """
    params = {'degree': [2, 3, 4, 5]}
    model = KernelRidge(kernel = 'poly')
    classifier = GridSearchCV(model, params)
    classifier.fit(X_data, y_data)
    best_params = classifier.best_params_
    degree = best_params['degree']
    return degree

def predict_function(x, y, degree):
    x = x.reshape(x.shape[0], )
    poly = np.polyfit(x = x, y = y, deg = degree)
    string = 'Function: '
    total = degree
    for i in range(degree + 1):
        if round(poly[i], 2) != 0.:
            string = string + " + x^{} * {}".format(total, round(poly[i], 2))
        total -= 1
    return string

#test it
X_data = np.array( [-1.2, -0.01, 1.23, 1.8, 20, 21, 22, 23.1, 123])
X_data = X_data.reshape(X_data.shape[0], 1)
y_data = np.array([526.8246347954033,
 16.934384611296693,
 34.90225474157847,
 53.19035775656099,
 1041679.9259436745,
 1293754.150079261,
 1588916.0855719403,
 1968905.8269523252,
 2121261427.2929053])

print(predict_function(X_data, y_data, predict_degrees(X_data, y_data)))
