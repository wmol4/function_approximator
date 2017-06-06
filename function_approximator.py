import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.kernel_ridge import KernelRidge

def predict_degrees(x, y):
    """
    predict how many degrees are represented by polynomial data
    """
    x = x.reshape(-1, 1)
    params = {'degree': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    model = KernelRidge(kernel = 'poly')
    classifier = GridSearchCV(model, params)
    classifier.fit(x, y)
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
            if len(string) == 10:
                string = string + "{}*x^{}".format(round(poly[i], 2), total)
            elif total == 0:
                string = string + " + {}".format(round(poly[i], 2))
            else:
                string = string + " + {}*x^{}".format(round(poly[i], 2), total)
        total -= 1
    return string
    
def print_function(x, y):
    x = np.array(x)
    y = np.array(y)
    degree = predict_degrees(x, y)
    string = predict_function(x, y, degree)
    return string


#test it
X_data = [-1.2, -0.01, 1.23, 1.8, 20, 21, 22, 23.1, 123]
y_data = [526.8246347954033,
 16.934384611296693,
 34.90225474157847,
 53.19035775656099,
 1041679.9259436745,
 1293754.150079261,
 1588916.0855719403,
 1968905.8269523252,
 2121261427.2929053]

print(print_function(X_data, y_data)) #prints: Function: 9.87*x^4 + -75.4*x^3 + 169.14*x^2 + -97.05*x^1 + 16.03
#the data above actually represents:  π^2 x^4 - 24 π x^3 + 8 π x^2 + 144 x^2 - 97 x + 16
