import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

class LPSolver:
    def __init__(self):
        self.c = None  # Objective function coefficients
        self.A = None  # Constraints coefficients matrix
        self.b = None  # Constraints bounds
        self.bounds = None  # Variable bounds

    def set_objective(self, c):
        
        self.c = [-val for val in c]  # Negate for maximization

    def set_constraints(self, A, b):
        
        self.A = A
        self.b = b

    def set_variable_bounds(self, bounds):
       
        self.bounds = bounds

    def solve(self):
        
        if self.c is None or self.A is None or self.b is None or self.bounds is None:
            raise ValueError("Objective function, constraints, and bounds must be set before solving.")
        
        result = linprog(self.c, A_ub=self.A, b_ub=self.b, bounds=self.bounds, method='highs')

        if result.success:
            print(f"Optimal solution found:")
            print(f"Product A (x1): {result.x[0]:.2f}")
            print(f"Product B (x2): {result.x[1]:.2f}")
            print(f"Maximum Profit: Rs {-result.fun:.2f}")
        else:
            print("No solution found")
        
        return result

    def plot_feasible_region(self, x_range):
        
        if len(self.A[0]) != 2:
            print("Visualization only supported for 2 variables.")
            return

        x1 = np.linspace(x_range[0], x_range[1], 400)

        
        y1 = (self.b[0] - self.A[0][0] * x1) / self.A[0][1]  # First constraint
        y2 = (self.b[1] - self.A[1][0] * x1) / self.A[1][1]  # Second constraint
        y3 = (self.b[2] - self.A[2][0] * x1) / self.A[2][1]  # Third constraint

        y1 = np.clip(y1, 0, None)
        y2 = np.clip(y2, 0, None)
        y3 = np.clip(y3, 0, None)

        plt.plot(x1, y1, label='Constraint 1', color='r')
        plt.plot(x1, y2, label='Constraint 2', color='g')
        plt.plot(x1, y3, label='Constraint 3', color='b')

        plt.fill_between(x1, np.minimum(np.minimum(y1, y2), y3), color='gray', alpha=0.3)

        
        plt.xlim(x_range[0], x_range[1])
        plt.ylim(0, max(self.b))
        plt.xlabel('Product A (x1)')
        plt.ylabel('Product B (x2)')
        plt.title('Feasible Region for Production of Products A and B')
        plt.legend()

        plt.grid(True)
        plt.show()


# Example Usage
if __name__ == "__main__":
    solver = LPSolver()

    # Set the objective function coefficients (profits)
    solver.set_objective([6, 5])

    # Set the constraints coefficients and bounds
    A = [
        [0, 2],  
        [1, 2],  
        [1, 1],  
    ]
    b = [45, 30, 18]  
    solver.set_constraints(A, b)

    solver.set_variable_bounds([(0, None), (0, None)])

    result = solver.solve()

    solver.plot_feasible_region((0, 30))













