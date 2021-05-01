from typing import List


def minPathSum(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    dp = [[0]*cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    for i in range(1, rows):
        dp[i][0] = dp[i-1][0]+grid[i][0]

    for i in range(1, cols):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])

    print(dp)
    return dp[rows-1][cols-1]


if __name__ == '__main__':
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    #Output: 7
    # Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
    print(minPathSum(grid))

    grid = [[1, 2, 3], [4, 5, 6]]
    #Output: 12
    print(minPathSum(grid))
