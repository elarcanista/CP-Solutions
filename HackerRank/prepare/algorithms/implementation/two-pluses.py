# https://www.hackerrank.com/challenges/two-pluses/
from copy import deepcopy

def check_available(grid, rows, cols, r, c, size):
    up, down = r - size, r + size
    left, right = c - size, c + size
    inside_grid = up >= 0 and down < rows and left >= 0 and right < cols
    if not inside_grid:
        return False
    corners_good = grid[up][c] and grid[down][c] and grid[r][left] and grid[r][right]
    if not corners_good:
        return False
    grid[up][c], grid[down][c], grid[r][left], grid[r][right] = False, False, False, False
    return True

def brute_force(grid, rows, cols, crosses):
    if crosses == 0:
        return 1
    goal = 0
    for r in range(rows):
        for c in range(cols):
            size = 0
            new_grid = deepcopy(grid)
            while check_available(new_grid, rows, cols, r, c, size):
                subgoal = brute_force(new_grid, rows, cols, crosses - 1)
                goal = max(goal, subgoal * (size * 4 + 1))
                size += 1
    return goal

rows, cols = map(int, input().split())
grid = []
for _ in range(rows):
    grid.append([c == 'G' for c in input()])
print(brute_force(grid, rows, cols, 2))
