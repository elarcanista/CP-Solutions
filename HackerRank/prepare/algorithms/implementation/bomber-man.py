# https://www.hackerrank.com/challenges/bomber-man/
from copy import deepcopy
def neighbours(rows, columns, r, c):
    ans = [(r, c)]
    if r > 0:
        ans.append((r-1, c))
    if r < rows - 1:
        ans.append((r+1, c))
    if c > 0:
        ans.append((r, c-1))
    if c < columns - 1:
        ans.append((r, c+1))
    return ans

def step(grid, rows, columns, detonate):
    new_grid = deepcopy(grid)
    for r in range(rows):
        for c in range(columns):
            if not detonate:
                new_grid[r][c] += 1
                continue
            if grid[r][c] == 2:
                for i, j in neighbours(rows, columns, r, c):
                    new_grid[i][j] = 0
    return new_grid

def pretty_print(grid, from_bin):
    for r in grid:
        print("".join(map(lambda c: from_bin[c], r)))

def simulate(n, grid, r, c):
    if n == 1:
        return grid
    grid = step(grid, r, c, False)
    if n == 2:
        return grid
    for t in range((n - 3) % 4 + 1):
        grid = step(grid, r, c, t % 2 == 0)
    return grid

r, c, n = map(int, input().split())
grid = []
to_bin = {'.': 0, 'O': 1}
from_bin = ['.', 'O', 'O']
for _ in range(r):
    grid.append([to_bin[c] for c in input()])
pretty_print(simulate(n, grid, r, c), from_bin)
