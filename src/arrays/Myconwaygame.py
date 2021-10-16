def conwayGame(grid):

    rows = len(grid)
    cols = len(grid[0])

    newgrid = [[0 for r in range(rows)] for c in range(cols)]
    
    directions = [(1,0),(-1,0),(0,-1),(0,1),(1,1),(-1,1),(1,-1),(-1,-1)]
    for r in range(rows):
        for c in range(cols):
            totals = 0
            for x,y in directions:
                rx = x+r
                cx = y+c
                if rx<rows and cx<cols:
                    totals+=grid[rx][cx]
                         
            
            if grid[r][c]==1 and (totals<2 or totals>3):
                    newgrid[r][c]=0
            elif grid[r][c]==1  and 2<=totals<=3 or (grid[r][c]==0 and totals==3):
                newgrid[r][c]=1
            
            print(newgrid)

    #print(newgrid)
    return newgrid

        






                       
if __name__=='__main__':

    grid = [[0,0,0,0],
            [0,1,0,0],
            [0,1,0,0],
            [0,1,0,0]]

    print(conwayGame(grid))
    print(conwayGame(conwayGame(grid)))

