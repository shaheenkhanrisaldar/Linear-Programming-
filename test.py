
from transportation import vogels_approximation_method, least_cost_cell_method, north_west_corner_method
from assignment import hungarian_algorithm 
'''
Transportation problem example:
Each cell in the cost_matrix represents the number of hours it takes to finish a game
for a given worker (rows) on a specific game (columns).

Supply: Number of hours each player has available.
Demand: Number of hours needed to complete each game.
The objective is to minimize the total hours spent 
'''

# Define your cost matrix, supply, and demand here
cost_matrix = [[21,16,25,13],
               [17,18,14,23],
               [32,27,18,41]]
supply = [11,13,19]
demand = [6,10,12,15]

print("Vogel's Approximation Method:")
vogels_approximation_method(cost_matrix, supply, demand)

#print("\nLeast Cost Cell Method:")
#least_cost_cell_method(cost_matrix, supply, demand)

#print("\nNorth-West Corner Method:")
#north_west_corner_method(cost_matrix, supply, demand)
