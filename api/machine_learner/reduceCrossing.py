import pandas as pd
import numpy as np
import itertools
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import json

#*****
#This approach adapts the edge crossing minimization method (https://arxiv.org/abs/1210.2041 and https://dankerrigan.me/algs-2-project/)  for parallel coordinates 
#*****

# Load the CSV file
file_path = '../api/dataset/rounded_fairness_metrics_results.csv'
df = pd.read_csv(file_path)

# Normalize data
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])

# Function to count crossings between two adjacent axes
def count_crossings(df, axis1, axis2):
    crossings = 0
    for i, j in itertools.combinations(range(len(df)), 2):
        x1 = df.iloc[i][axis1]
        x2 = df.iloc[j][axis1]
        y1 = df.iloc[i][axis2]
        y2 = df.iloc[j][axis2]
        if (x1 - x2) * (y1 - y2) < 0:
            crossings += 1
    return crossings

# Function to calculate total crossings for a given order of axes
def total_crossings(df, order):
    crossings = 0
    for i in range(len(order) - 1):
        crossings += count_crossings(df, order[i], order[i + 1])
    return crossings

# Function to optimize the axis order
def optimize_axis_order(df):
    n = len(df.columns)
    
    # Objective function to minimize
    def objective(order):
        order = np.argsort(order)
        return total_crossings(df, order)
    
    # Initial guess
    initial_order = np.arange(n)
    
    # Bounds for the optimization
    bounds = [(0, n-1) for _ in range(n)]
    
    # Optimization
    result = minimize(objective, initial_order, bounds=bounds, method='L-BFGS-B') #optimization algorithm used by the scipy.optimize.minimize function
    
    # Get the optimized order
    optimized_order = np.argsort(result.x)
    optimized_order_column = df.columns[optimized_order]
    optimized_order_indices_json = json.dumps(optimized_order_column.tolist())
    return optimized_order_indices_json

# # Find optimized order
#optimized_order = optimize_axis_order(df)
# optimized_order = df.columns[optimized_order_indices]

# print(optimized_order)

#print(optimized_order)

