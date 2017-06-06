# function_approximator
Use sklearn and numpy to approximate polynomials quickly

# example 1
````
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
          
print(print_function(X_data, y_data)) #Function: 9.87*x^4 + -75.4*x^3 + 169.14*x^2 + -97.05*x^1 + 16.03
````
# example 2
````
X_data = [1, 2, 3, 4, 5]
y_data = [1, 4, 9, 16, 25]

print(print_function(X_data, y_data)) #Function: 1.0*x^2
````
