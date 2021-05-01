
from typing import List


def numIslands(grid: List[List[str]]) -> int:

    if not grid:
        return 0

    numIsland = 0
    visited = set()

    rows = len(grid)
    cols = len(grid[0])

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(matrix, row, col):
        visited.add((row, col))
        #matrix[row][col] = -1
        for d in directions:
            r = row+d[0]
            c = col+d[1]

            if r in range(rows) and c in range(cols) and (r, c) not in visited and matrix[r][c] == '1':
                #visited.add((r, c))
                dfs(matrix, r, c)

        return

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1' and (row, col) not in visited:
                numIsland += 1
                dfs(grid, row, col)

    return numIsland


if __name__ == '__main__':

    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    #Output: 1
    print(numIslands(grid))

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]  # Output: 3

    print(numIslands(grid))
