import numpy as np

# Define a 9x9 Sudoku grid with zeros representing empty cells
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def possible(y, x, n):
    """Check if number n can be placed at position (y, x) in the grid."""
    global grid
    # Check row and column
    for i in range(0, 9):
        if grid[y][i] == n or grid[i][x] == n:
            return False
    # Check 3x3 subgrid
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True

def solve():
    """Solve the Sudoku puzzle using backtracking."""
    global grid
    for y in range(9):
        for x in range(9):
            # Find an empty cell
            if grid[y][x] == 0:
                # Try placing numbers 1-9 in the empty cell
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        if solve():  # Recursive call to continue solving
                            return True
                        grid[y][x] = 0  # Reset cell for backtracking
                return False  # Trigger backtracking if no number fits
    return True  # Solved successfully

# Run the solver and print the final grid
if solve():
    print(np.matrix(grid))
else:
    print("No solution exists")