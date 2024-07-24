import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.optimize import minimize
import json

# #*****
# #This approach adapts the edge crossing minimization method (https://arxiv.org/abs/1210.2041 and https://dankerrigan.me/algs-2-project/)  for parallel coordinates 
# #*****

file_path = '../api/dataset/rounded_fairness_metrics_results.csv'
df = pd.read_csv(file_path)

# Normalize the data
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])

#Counts the number of line crossings between two axes 
#(To determine how many times lines connecting data points between two axes intersect (or cross each other).)
def count_crossings(df, axis1, axis2):
    crossings = 0
    num_points = len(df)
    for i in range(num_points):
            for j in range(i + 1, num_points):
                # Check if the lines between the points on the two axes cross
                if (df.iloc[i, axis1] - df.iloc[j, axis1]) * (df.iloc[i, axis2] - df.iloc[j, axis2]) < 0:
                    crossings += 1
                
    return crossings

#Calculates the total number of crossings for a given order of axes.
def total_crossings(df, order):
    total = 0
    for i in range(len(order) - 1):
        total += count_crossings(df, order[i], order[i + 1])
    return total

#Objective function to minimize the total crossings.
def objective(order, df):
    order = np.argsort(order)
    return total_crossings(df, order)

#Finds the optimal order of axes to minimize crossings.
def optimize_axis_order(df):
    num_axes = len(df.columns)
    
    # Initial guess for the optimization
    initial_guess = np.arange(num_axes)
    
    # Bounds for each axis index
    #bounds = [(0, num_axes - 1) for _ in range(num_axes)]
    lower_bound = 0
    upper_bound = num_axes - 1
    bounds = [(lower_bound, upper_bound) for _ in range(num_axes)]

    result = minimize(objective, initial_guess, args=(df,), bounds=bounds, method='L-BFGS-B')  #optimization algorithm used by the scipy.optimize.minimize function
    
    # result.x gives the order that results in the fewest crossings. .x Contains the solution array (optimized values of the variables).
    print(result.x)
    optimized_order = np.argsort(result.x)
    #print(optimized_order)
    optimized_order_column = df.columns[optimized_order]
    optimized_order_json = json.dumps(optimized_order_column.tolist())
    
    return optimized_order_json

# Get the optimized order of axes
optimized_order_indices_json = optimize_axis_order(df)

# Print the JSON string
print(optimized_order_indices_json)

