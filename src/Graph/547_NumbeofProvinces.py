from typing import List


def findCircleNum(isConnected: List[List[int]]) -> int:

    if not isConnected:
        return 0

    visited = set()
    numOfProvinces = 0

    def dfs(start):
        visited.add(start)

        for end in range(len(isConnected)):
            if isConnected[start][end] == 1 and end not in visited:
                dfs(end)

    for start in range(len(isConnected)):
        if start not in visited:
            numOfProvinces += 1
            dfs(start)

    return numOfProvinces


if __name__ == '__main__':
    isConnected = [[1, 0, 0, 1],
                   [0, 1, 1, 0],
                   [0, 1, 1, 1],
                   [1, 0, 1, 1]]
    print(findCircleNum(isConnected))  # 1

    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(findCircleNum(isConnected))  # 2
