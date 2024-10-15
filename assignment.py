import numpy as np
from scipy.optimize import linear_sum_assignment

def hungarian_algorithm(cost_matrix):
  
    
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    assignments = [(row, col) for row, col in zip(row_ind, col_ind)]
    
    # Calculate the total cost based on the optimal assignment
    total_cost = cost_matrix[row_ind, col_ind].sum()

    return assignments, total_cost

def input_cost_matrix():
    n = int(input("Enter the number of workers (rows): "))
    m = int(input("Enter the number of jobs (columns): "))

    print(f"Enter the cost matrix ({n} x {m}):")
    cost_matrix = []
    for i in range(n):
        row = list(map(int, input(f"Enter costs for worker {i+1} (space-separated): ").split()))
        cost_matrix.append(row)

    return np.array(cost_matrix)  # Convert to NumPy array

def solve_assignment_problem():
    
    cost_matrix = input_cost_matrix()  # Get cost matrix from user input
    assignments, total_cost = hungarian_algorithm(cost_matrix)

    print("\nOptimal Assignments (Worker -> Job):")
    for worker, job in assignments:
        print(f"Worker {worker + 1} is assigned to Job {job + 1}")

    print(f"\nTotal Minimum Cost: {total_cost}")

