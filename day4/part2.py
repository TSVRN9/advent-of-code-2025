import copy

def check_neighbors(i: int, j: int, grid: list[list[str]]) -> bool:
    m = len(grid)
    n = len(grid[0])

    count_dots = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '.':
                count_dots += 1
                if count_dots >= 5:
                    return True
    return False

# mutates grid
def simulate_grid(grid: list[list[str]]) -> int:
    count = 0
    g = copy.deepcopy(grid) # keep copy for reference

    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == "@" and check_neighbors(i, j, g):
                count += 1
                grid[i][j] = '.'
    
    return count



with open('day4/input.txt') as f:
    grid = list(map(lambda l: list(l.strip()), f.readlines()))
    count = 0
    while (c := simulate_grid(grid)) != 0:
        count += c
    
print(count)