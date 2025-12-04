grid: list[list[str]] = []
count = m = n = 0

def check_neighbors(i: int, j: int) -> bool:
    count_dots = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '.':
                count_dots += 1
                if count_dots >= 5:
                    return True
    return False


with open('day4/input.txt') as f:
    grid = list(map(lambda l: list(l.strip()), f.readlines()))
    m = len(grid)
    n = len(grid[0])

    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == "@" and check_neighbors(i, j):
                count += 1
                grid[i][j] = 'x'

    
print(count)