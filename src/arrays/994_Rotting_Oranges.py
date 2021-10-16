from collections import deque

def OrangesRotting(grid):
    

    rows = len(grid)
    cols = len(grid[0])
    
    queue = deque()

    def bfs(q,grid):
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        res = 0
        while q:
            r,c,time = q.popleft()
            res = time
            print(f'row = {r} col = {c} time ={res}')
            #print(q)
            print(grid)
            for dx,dy in directions:
                row = r+dx
                col = c+dy
                if row in range(rows) and col in range(cols) and grid[row][col] ==1:
                    queue.append((row,col,time+1))
                    grid[row][col]=2
        return res

              
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] ==2 :
                queue.append((r,c,0))

    print(queue)            
    res = bfs(queue,grid) 
    print(res)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] ==1 :
                return -1

    return res


if __name__ == '__main__':
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(OrangesRotting(grid))

    grid = [[2,1,1],[0,1,1],[1,0,1]]
    #Output: -1
    print(OrangesRotting(grid))

    grid = [[0,2]]
    #Output: 0
    print(OrangesRotting(grid))