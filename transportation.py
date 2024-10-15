
import numpy as np

INF = 10**3

# function for finding the row difference and column difference
def find_diff(grid):
    row_diff = []
    col_diff = []
    for i in range(len(grid)):
        arr = grid[i][:]
        arr.sort()
        row_diff.append(arr[1] - arr[0] if len(arr) > 1 else arr[0])  # Handle single element row edge case
    for col in range(len(grid[0])):
        arr = [grid[i][col] for i in range(len(grid))]
        arr.sort()
        col_diff.append(arr[1] - arr[0] if len(arr) > 1 else arr[0])  # Handle single element column edge case
    return row_diff, col_diff

# Function to solve Vogel's Approximation Method
def vogels_approximation_method(cost_matrix, supply, demand):
    n = len(cost_matrix)
    m = len(cost_matrix[0])
    ans = 0
    allocation = [[0] * m for _ in range(n)]  

    while max(supply) != 0 or max(demand) != 0:
        row, col = find_diff(cost_matrix)
        maxi1 = max(row)
        maxi2 = max(col)
        if maxi1 >= maxi2:
            for ind, val in enumerate(row):
                if val == maxi1:

                    mini1 = min(cost_matrix[ind])
                    for ind2, val2 in enumerate(cost_matrix[ind]):
                        if val2 == mini1:
                            mini2 = min(supply[ind], demand[ind2])  # Find the min between supply and demand
                            ans += mini2 * mini1 
                            allocation[ind][ind2] = mini2  
                            supply[ind] -= mini2  
                            demand[ind2] -= mini2  
                            if demand[ind2] == 0:
                                for r in range(n):
                                    cost_matrix[r][ind2] = INF  
                            if supply[ind] == 0:
                                cost_matrix[ind] = [INF for _ in range(m)]  
                            break
                    break

        
        else:
            for ind, val in enumerate(col):
                if val == maxi2:
                    
                    mini1 = INF
                    for j in range(n):
                        mini1 = min(mini1, cost_matrix[j][ind])

                    for ind2 in range(n):
                        if cost_matrix[ind2][ind] == mini1:
                            mini2 = min(supply[ind2], demand[ind])
                            ans += mini2 * mini1  
                            allocation[ind2][ind] = mini2  
                            supply[ind2] -= mini2  
                            demand[ind] -= mini2

                            if demand[ind] == 0:
                                for r in range(n):
                                    cost_matrix[r][ind] = INF  
                            if supply[ind2] == 0:
                                cost_matrix[ind2] = [INF for _ in range(m)]  
                            break
                    break
    print("The basic feasible solution is:", ans)
    print("The allocation matrix is:")
    for row in allocation:
        print(row)


# Least Cost Cell Method to calculate the initial feasible solution
def least_cost_cell_method(cost_matrix, supply_amounts, demand_amounts):
    
    cost_matrix = np.array(cost_matrix)  
    supply = np.array(supply_amounts)
    demand = np.array(demand_amounts)

    total_cost = 0

    allocation_matrix = np.zeros_like(cost_matrix)

   
    processed_cells = np.zeros_like(cost_matrix, dtype=bool)

    while supply.sum() > 0 and demand.sum() > 0:
        least_cost = np.inf  
        row, col = -1, -1  
        for i in range(cost_matrix.shape[0]):  
            for j in range(cost_matrix.shape[1]):
                if not processed_cells[i, j] and cost_matrix[i, j] < least_cost:
                    least_cost = cost_matrix[i, j]
                    row, col = i, j

        if row == -1 or col == -1:
            break  

        allocation = min(supply[row], demand[col])

        total_cost += allocation * cost_matrix[row, col]

        supply[row] -= allocation
        demand[col] -= allocation

        allocation_matrix[row, col] = allocation

        if supply[row] == 0:
            processed_cells[row, :] = True  
        if demand[col] == 0:
            processed_cells[:, col] = True  

    print("The basic feasible solution is:", total_cost)
    print("The allocation matrix is:")
    for row in allocation_matrix:
        print(row)


# North-West Corner Method (stub)
def north_west_corner_method(cost_matrix, supply, demand):
    # Create a local copy
    n = len(cost_matrix)
    m = len(cost_matrix[0])
    allocation = [[0] * m for _ in range(n)]
    total_cost = 0

    row, col = 0, 0

    while row < n and col < m:
        
        allocation_amount = min(supply[row], demand[col])
        allocation[row][col] = allocation_amount
        total_cost += allocation_amount * cost_matrix[row][col]

        supply[row] -= allocation_amount
        demand[col] -= allocation_amount

        if supply[row] == 0:
            row += 1
        if demand[col] == 0:
            col += 1

    print("The basic feasible solution is:", total_cost)
    print("The allocation matrix is:")
    for row in allocation:
        print(row)

def input_transport_problem():
    
    n = int(input("Enter the number of suppliers (rows): "))
    m = int(input("Enter the number of consumers (columns): "))

    print(f"Enter the cost matrix ({n} x {m}):")
    cost_matrix = []
    for i in range(n):
        row = list(map(int, input(f"Enter costs for supplier {i+1} (space-separated): ").split()))
        cost_matrix.append(row)

    supply = list(map(int, input("Enter supply values (space-separated): ").split()))
    demand = list(map(int, input("Enter demand values (space-separated): ").split()))

    return cost_matrix, supply, demand

def solve_transport_problem():
    
    cost_matrix, supply, demand = input_transport_problem()
    print("\n---Vogel's Approximation Method---")
    vogels_approximation_method(cost_matrix, supply.copy(), demand.copy())
    
    print("\n---Least Cost Cell Method---")
    least_cost_cell_method(cost_matrix, supply.copy(), demand.copy())
    
    print("\n---North-West Corner Method---")
    north_west_corner_method(cost_matrix, supply.copy(), demand.copy())
