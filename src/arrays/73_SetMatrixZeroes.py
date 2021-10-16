def setZeroes(matrix):

    rows = set()
    cols = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] ==0:
                rows.add(r)
                cols.add(c)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in rows or c in cols:
                matrix[r][c]=0

    return matrix
    
if __name__ =='__main__':
    matrix = [[1,1,1],
              [1,0,1],
              [1,1,1]]
    '''Out: [[1,0,1],
             [0,0,0],
             [1,0,1]] '''
    print(setZeroes(matrix))