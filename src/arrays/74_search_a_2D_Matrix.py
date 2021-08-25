def searchMatrix(matrix,target):

    rows , cols = len(matrix),len(matrix[0])

    toprows=0 
    botrows=rows-1

    while toprows <= botrows:
        row = (toprows+botrows)//2

        if target > matrix[row][-1]:
            toprows = row+1
        elif target < matrix[row][0]:
            botrows=row-1
        else:
            break

    if not toprows<=botrows:
        return False

    row = (toprows+botrows)//2

   
    low=0
    high=cols-1
    
    while low <= high:
        mid = (low+high)//2
        
        if target > matrix[row][mid]:
            low = mid +1
        elif target < matrix[row][mid]:
            high = mid-1
        else:
            return True
            
    return False


if __name__=='__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    #Output: true
    print(searchMatrix(matrix,target))

    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    #Output: false
    print(searchMatrix(matrix,target))

    matrix = [[1,3]]
    target = 3

    print(searchMatrix(matrix,target))